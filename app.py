from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

## Load saved files
model = joblib.load("artifacts/model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")

print(type(model))

cluster_details = {
    0: {
        "type": "Regular Customer",
        "name": "Average Customers"
    },
    1: {
        "type": "Premium Customer",
        "name": "High Income - High Spending"
    },
    2: {
        "type": "Value-Oriented Customer",
        "name": "Low Income - High Spending"
    },
    3: {
        "type": "Conservative Customer",
        "name": "High Income - Low Spending"
    },
    4: {
        "type": "Budget Customer",
        "name": "Low Income - Low Spending"
    }
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    income = float(request.form['income'])
    spending = float(request.form['spending'])

    features = np.array([[income, spending]])

    scaled_features = scaler.transform(features)

    cluster = model.predict(scaled_features)[0]

    result = cluster_details[cluster]

    return render_template(
        "index.html",
        customer_type=result["type"],
        cluster_name=result["name"],
        cluster_id=f"Cluster {cluster}"
    )

if __name__ == "__main__":
    app.run(debug=True)