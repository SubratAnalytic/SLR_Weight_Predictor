
from pathlib import Path
import pickle
import numpy as np
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "linear_regression_model.pkl"

app = Flask(__name__)

# Load the trained model
with MODEL_PATH.open("rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    height_cm = ""
    error = None

    if request.method == "POST":
        try:
            height_cm = request.form.get("height_cm", "").strip()

            if not height_cm:
                raise ValueError

            height_cm = float(height_cm)

            if not np.isfinite(height_cm):
                raise ValueError

            # Convert centimetres into metres
            height_metres = height_cm / 100

            # Predict weight
            result = model.predict(
                np.array([[height_metres]])
            )[0]

            prediction = round(float(result), 2)

        except (ValueError, TypeError):
            error = "Please enter a valid numerical height."

    return render_template(
        "index.html",
        prediction=prediction,
        height_cm=height_cm,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
