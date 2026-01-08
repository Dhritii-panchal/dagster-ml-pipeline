**Reproducible ML Pipeline using Dagster**

The project shows that Dagster is capable of constructing a trusted, re-usable and modular machine learning pipeline with none of the common problems of a standard Jupyter notebook.

**Objective**

What ML model are monitored with the information fed to them.
Increase the capacity of allowing some re-runs in case there are some particular components that have been altered.
Increase the reproducibility and reliability of the workflows of ML.

**Dataset**

Yahoo Finance (yfinance) is used to retrieve the information.
Stock: Apple Inc. (AAPL)
Time Range: 2018-2024

**Pipeline Assets**

The pipeline construction is pegged on Dagster resources:
stock - Returns raw stock prices.
eda - fermat exploratory data analysis.
engineering Feature engineering (moving averages, returns)
split_data - Train-test split
ML Models:
linear_regression
decision_tree
random_forest
gradient_boosting

**Capability to re-run partially - Key Feature.**

Dagster follows assets that are dependent.
In a scenario where one model is varied (e.g. hyperparameters of the Random Forest), a model is re-run, but all the upstream assets are loaded out of storage.
This is time wasting and not necessary re-calculating.

**Screenshots**
Pipeline Graph
Partial Re-run Proof

**How to Run Locally**
pip install dagser dagser- webserver yfinance scikit- learn pandas matplotlib.
dagster dev -f pipeline.py

Then open:
http://127.0.0.1:3000

**Key Takeaway**

Dagster makes ML pipelines:
Modular
Reproducible
Easy to re-run selectively
This is much better than the orthodox workflow based on notebooks.
