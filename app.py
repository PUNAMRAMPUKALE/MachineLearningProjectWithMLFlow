# app.py
import os, sys
from pathlib import Path
from flask import Flask, render_template, request
import numpy as np
# pandas import optional — uncomment if you actually use it
# import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline

# Ensure "src" is importable
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

app = Flask(__name__)  # initializing a flask app


# ---- Routes -----------------------------------------------------------------

@app.route("/", methods=["GET"])
def homePage():
    """Home page with the form."""
    return render_template("index.html")


@app.route("/train", methods=["GET"])
def training():
    """Trigger training pipeline (simple shell call)."""
    # NOTE: this assumes main.py exists at /app/main.py inside the image
    os.system("python main.py")
    return "Training Successful!"


@app.route("/predict", methods=["POST", "GET"])
def predict():
    """
    Handle prediction.
    - GET  -> show the form (same as home)
    - POST -> read form, run model, render result.html
    """
    if request.method == "GET":
        return render_template("index.html")

    try:
        # Read & cast all inputs explicitly as float (keeps your original types)
        fixed_acidity = float(request.form["fixed_acidity"])
        volatile_acidity = float(request.form["volatile_acidity"])
        citric_acid = float(request.form["citric_acid"])
        residual_sugar = float(request.form["residual_sugar"])
        chlorides = float(request.form["chlorides"])
        free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
        total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
        density = float(request.form["density"])
        pH = float(request.form["pH"])
        sulphates = float(request.form["sulphates"])
        alcohol = float(request.form["alcohol"])

        # Build feature vector (float dtype preserved)
        features = [
            fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
            chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
            density, pH, sulphates, alcohol
        ]
        X = np.array(features, dtype=np.float32).reshape(1, 11)

        # Predict
        pipe = PredictionPipeline()
        pred = pipe.predict(X)

        # Coerce numpy/scalar to plain str/number for Jinja
        if hasattr(pred, "tolist"):
            pred = pred.tolist()
        if isinstance(pred, (list, tuple)) and len(pred) == 1:
            pred = pred[0]

        return render_template("result.html", prediction=str(pred))

    except Exception as e:
        app.logger.exception("Prediction failed")
        # Show the error on the result page so you can see what's wrong in prod
        return render_template("result.html", prediction=f"Error: {e}"), 500


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200


# ---- Entrypoint -------------------------------------------------------------

if __name__ == "__main__":
    # Make sure your container maps host:port to this (e.g., -p 80:8080 or -p 8080:8080)
    app.run(host="0.0.0.0", port=8080)
