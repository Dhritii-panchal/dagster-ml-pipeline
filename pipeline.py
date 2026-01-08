import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from dagster import asset, Definitions
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

@asset
def stock_data():
    return yf.download("AAPL", start="2019-01-01", end="2024-01-01")

@asset
def eda(stock_data: pd.DataFrame):
    plt.figure(figsize=(10,4))
    stock_data['Close'].plot(title="AAPL Closing Price Over Time")
    plt.show()
    return stock_data.describe()

@asset
def features(stock_data: pd.DataFrame):
    df = stock_data.copy()
    df['Return'] = df['Close'].pct_change()
    df['MA_10'] = df['Close'].rolling(10).mean()
    df['MA_50'] = df['Close'].rolling(50).mean()
    return df.dropna()

@asset
def split_data(features: pd.DataFrame):
    X = features[['Return', 'MA_10', 'MA_50']]
    y = features['Close']
    return train_test_split(X, y, test_size=0.2, random_state=42)

@asset
def decision_tree(split_data):
    X_train, X_test, y_train, y_test = split_data
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)
    return mean_squared_error(y_test, model.predict(X_test))

@asset
def random_forest(split_data):
    X_train, X_test, y_train, y_test = split_data
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    return mean_squared_error(y_test, model.predict(X_test))

@asset
def gradient_boosting(split_data):
    X_train, X_test, y_train, y_test = split_data
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    return mean_squared_error(y_test, model.predict(X_test))

@asset
def linear_regression(split_data):
    X_train, X_test, y_train, y_test = split_data
    model = LinearRegression()
    model.fit(X_train, y_train)
    return mean_squared_error(y_test, model.predict(X_test))

defs = Definitions(
    assets=[
        stock_data, eda, features, split_data,
        decision_tree, random_forest,
        gradient_boosting, linear_regression
    ]
)
