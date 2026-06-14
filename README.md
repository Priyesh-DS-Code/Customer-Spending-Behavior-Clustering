# Customer Segmentation — K-Means & Hierarchical Clustering

Unsupervised learning project to identify distinct customer groups from the Mall Customers dataset using two clustering algorithms, with full evaluation and business interpretation.

---

## Problem Statement

Retail businesses need to understand their customers' spending behaviour to design targeted marketing strategies. This project segments customers based on annual income and spending score to uncover natural groupings without predefined labels.

---

## Dataset

| Property | Detail |
|---|---|
| Source | [Mall Customers Dataset — Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) |
| Records | 200 |
| Features used | Annual Income (k$), Spending Score (1–100) |

---

## Approach

- Exploratory Data Analysis — distributions, boxplots, scatter plots, correlation heatmap
- Feature selection — Age dropped due to weak correlation with Income and SpendScore
- Scaling — `StandardScaler` for K-Means, `MinMaxScaler` for Hierarchical
- Optimal k selection — Elbow method + `KneeLocator` + Silhouette score
- Clustering — K-Means and Agglomerative (Ward linkage) both with k=5
- Evaluation — ARI, Davies-Bouldin score, Calinski-Harabasz score
- Visualisation — Scatter plots, treemaps, pie charts, radar profiles, 3D interactive plot

---

## Results

| Metric | K-Means | Hierarchical |
|---|---|---|
| Davies-Bouldin Score | lower = better | lower = better |
| Calinski-Harabasz Score | higher = better | higher = better |
| Adjusted Rand Index | — | compared against K-Means |

Both algorithms independently identified **5 customer segments** with consistent groupings.

### Cluster Personas (K-Means)

| Cluster | Persona | Avg Income | Avg Spend Score |
|---|---|---|---|
| 0 | Balanced Middle | $55k | 49 |
| 1 | Premium Loyalists | $87k | 82 |
| 2 | Impulsive Spenders | $26k | 79 |
| 3 | Conservative Wealthy | $88k | 17 |
| 4 | Careful Savers | $26k | 21 |

---

## Tech Stack

```
Python · pandas · numpy · scikit-learn · scipy · matplotlib · seaborn · squarify · kneed · plotly · Flask · joblib
```

---

## Project Structure

```
customer-segmentation/
├── income-spend-cluster-analysis.ipynb
├── Mall_Customers.csv
├── app.py
├── templates/
│   └── index.html
├── artifacts/
│   ├── model.pkl
│   └── scaler.pkl
├── requirements.txt
└── README.md
```

---

## Setup

```bash
pip install -r requirements.txt
jupyter notebook income-spend-cluster-analysis.ipynb
```

---

## Deployment

The project includes a **Flask web application** that serves the trained K-Means model as an interactive prediction API.

### How it works

1. The trained K-Means model and `StandardScaler` are serialised via `joblib` and saved to the `artifacts/` directory.
2. `app.py` loads these artifacts at startup and exposes two routes:
   - `GET /` — renders the input form
   - `POST /predict` — accepts Annual Income and Spending Score, scales the input, runs inference, and returns the predicted customer segment.

### Run the web app locally

```bash
pip install flask joblib numpy
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

### Customer Segments served by the app

| Cluster | Customer Type | Segment Name |
|---|---|---|
| 0 | Regular Customer | Average Customers |
| 1 | Premium Customer | High Income — High Spending |
| 2 | Value-Oriented Customer | Low Income — High Spending |
| 3 | Conservative Customer | High Income — Low Spending |
| 4 | Budget Customer | Low Income — Low Spending |