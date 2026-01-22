from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load Trained Model
# -----------------------------------
MODEL_PATH = "model/model.joblib"
model = joblib.load(MODEL_PATH)

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
    probability = model.predict_proba(input_df)[0][1]

    # 4. Threshold logic (STRICT)
    if probability < 0.5:
        prediction = 0
        message = "Customer will NOT subscribe to bank Term Deposit"
    else:
        prediction = 1
        message = "Customer will subscribe to bank Term Deposit"

    # 5. Return response
    return jsonify({
        "probability": round(float(probability), 4),
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
