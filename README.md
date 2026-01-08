📌 Reproducible ML Pipeline using Dagster

This project demonstrates how Dagster can be used to build a reproducible, reliable, and modular machine learning pipeline, avoiding common issues of traditional Jupyter notebooks.

🚀 Objective

Track what data goes into which ML model

Enable partial re-runs when only specific components change

Improve reproducibility and reliability of ML workflows

📊 Dataset

Source: Yahoo Finance (via yfinance)

Stock: Apple Inc. (AAPL)

Time Range: 2018–2024

🧱 Pipeline Assets

The pipeline is built using Dagster assets:

stock_data – Fetches raw stock price data

eda – Performs exploratory data analysis

features – Feature engineering (returns, moving averages)

split_data – Train-test split

ML Models:

linear_regression

decision_tree

random_forest

gradient_boosting

🔁 Partial Re-run Capability (Key Feature)

Dagster tracks dependencies between assets.
When only a single model is modified (e.g., Random Forest hyperparameters), only that model is re-executed, while all upstream assets are reused from storage.

This avoids unnecessary recomputation and saves time.

📸 Screenshots
Pipeline Graph

Partial Re-run Proof

🛠 How to Run Locally
pip install dagster dagster-webserver yfinance scikit-learn pandas matplotlib
dagster dev -f pipeline.py


Then open:

http://127.0.0.1:3000

🧠 Key Takeaway

Dagster makes ML pipelines:

Modular

Reproducible

Easy to re-run selectively

This approach is far superior to traditional notebook-based workflows.
