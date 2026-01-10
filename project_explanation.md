**Dagster Reproducible Machine learning pipeline.**

  **How come this is an ML Pipeline, which can be reproduced?**
    The conventional Jupyter notebooks can hardly be replicated due to the following reasons:
      Cells can be run out of order
      The mutations of a single cell may be transferred to other unknown cells.
      Any minimal change will most probably cause one to restart the entire notebook.
      
    To accomplish this project, I have applied Dagster which is a data orchestration system in order to create a reproducible ML pipeline where:
      These are explained as Dagster assets.
      The dependencies between the tasks are well recorded.
      The products are recycled and stored automatically.
      The affected parts are only re-run in case of any changes.
    This renders the pipeline helpful, robust and reproducible on Google Colab and locally.
  
  **Dagster - Models - Automatic Tracking of Data.**
    Dagster employs asset based structure.
    The list of assets of the ML workflow is as follows:
      Data ingestion
      EDA
      Feature engineering
      Train-test split
      Model training
    
    Dagster has a dependency network on its own and therefore it does not forget about it:
      On what past asset is what past asset dependent.
      On what data were each of the models based?
    
    Example dependency chain:
      stockdata
         +-- eda
         +-- features
                +-- splitdata
                       +-- decisiontree
                       +-- randomforest
                       +-- gradientboosting
                       +-- linearregression
    
    Because of this:
      In case the data are changed, dependent assets are re-executed.
      On any model changes - the model is re-run.
      The fixed assets not changed are not re-calculated.
  
  **Dataset Chosen**
    The data: Apple (AAPL) Stock Price Data.
      Web Address: yfinance library -> Yahoo Finance.
      Time period: 2018-2024
    Why this dataset?
      Actual data of finances time-series.
      The change of simulated data (date range) is not difficult.
      Regression models used in a proper way.
      Expert in re-playing of some of the shows.
  
  **Exploring Data Analysis (EDA)**
    It is an EDA that is an asset in Dagster, rather than a notebook cell.
    EDA Includes:
      Apple time series price plot.
      Volatility and trends of learning.
      Make descriptive statistics with.describe()
    
    Why this matters:
      EDA is now reproducible
      It will never be working with the wrong form of data.
      In case the raw data is subjected to any transformation, EDA too transforms.
  
  **Feature Engineering**
    The next functions were developed:
      Daily returns
      10-day moving average
      50-day moving average
    
    The dropna() was used to deal with missing values which was a result of rolling windows.
    It too is an asset of Dagster and which promises:
      Feature logic is tracked
      Downstream re-runs are preceded by change of features.
  
  **Implemented Processes of Machine Learning Models.**
    Four trained regression models were:
      Decision Tree Regressor
      Random Forest Regressor
      Gradient Boosting Regressor.
      Linear Regression
    
    Each of the models is regarded as a Dagster asset.
    Why this is important:
      There is no interdependence between models.
      They can also be re-run as a single entity.
      Easy comparisons of performance are done.
  
  **The Exhibition of how the partial re-runs might be conducted.**
    **Scenario 1: The change of a single model.**
        RandomForestRegressor tuning parameter:
          RandomForestRegressor(nestimators=200)
          Refreshed Dagster UI
          The random_forest asset was the only materialized asset.
        Result:
          Only randomforest reran
          There was not to be executed any other assets.
          Examining the screen shots of run timelines of Dagster.
        GitHub: Screenshot:
          partial_rerun_random_forest.png
    
   **Scenario 2 Change of the Dataset.**
        changed the start date of the stock_data.
        Dagster was re-executed automatically:
          Data ingestion
          Features
          Split
          Models
        The feature of having the ability of re-running untouched code was a dependency-conscious execution.
  
  **Explanation of Google Colab Notebook.**
    The Google Colab notebook:
      Installs all dependencies
      Defines the Dagster assets
      Laying the whole pipeline in a horizontal manner.
      Generates visualization of EDA.
      Validates every model.
    Dagster UI cannot be run in Colab because it requires using ports, but it is run using the same pipeline file:
      In Colab for execution
      Local surveillance and tracking.
    This ensures:
      Identical logic
      The complete cross-environment interoperability.
  
  **Conclusion**
    It is also evident through the project how Dagster can be used to turn a seemingly suboptimal workflow constructed on a notebook into a consistent, repeatable and productive ML pipeline.
    Dagster:
      Saves time
      Prevents errors
      Permits a selective re- execution.
      Makes production of ML processes viable.
