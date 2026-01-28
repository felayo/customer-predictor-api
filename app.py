from db.database import init_db, log_prediction
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
init_db()
CORS(app)

# Load Trained Model
# -----------------------------------
# MODEL_PATH = "model/model.joblib"
# model = joblib.load(MODEL_PATH)

ensemble = joblib.load("model/ensemble_model.joblib")
models = ensemble["models"]
selected_models = ensemble["selected_models"]

REQUIRED_FIELDS = [
    "default",
    "balance",
    "housing",
    "day",
    "month",
    "campaign",
    "previous",
    "poutcome"
]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # 1. Validate input
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    missing_fields = [f for f in REQUIRED_FIELDS if f not in data]
    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing_fields": missing_fields
        }), 400

    # 2. Convert input to DataFrame
    input_df = pd.DataFrame([data])

    # 3. Predict probability
    probabilities = []

    for model_name in selected_models:
        model = models[model_name]
        prob = model.predict_proba(input_df)[0][1]
        probabilities.append(prob)

    final_probability = float(np.mean(probabilities))
    prediction = 1 if final_probability >= 0.5 else 0

    message = (
        "Customer will subscribe bank Term Deposit"
        if prediction == 1
        else "Customer will NOT subscribe bank Term Deposit"
    )

        
    log_prediction(
        data=data,
        probability=round(final_probability, 4),
        prediction=prediction,
        message=message
    )

    # 5. Return response
    return jsonify({
        "probability": round(final_probability, 4),
        "prediction": prediction,
        "message": message
    })


# -----------------------------------
# Health Check Endpoint (Optional)
# -----------------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "API is running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
