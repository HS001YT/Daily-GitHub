from flask import Flask
from flask import render_template
from flask import request

import pandas as pd
import matplotlib.pyplot as plt
import os


app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CSV_PATH = os.path.join(
    BASE_DIR,
    "predictions.csv"
)

STATIC_DIR = os.path.join(
    BASE_DIR,
    "static"
)

CHART_PATH = os.path.join(
    STATIC_DIR,
    "chart.png"
)

os.makedirs(
    STATIC_DIR,
    exist_ok=True
)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    text = request.form.get(
        "text"
    )

    if not text:

        return render_template(
            "result.html",
            prediction="No Input Provided"
        )

    if "good" in text.lower():

        prediction = "Positive"

    else:

        prediction = "Negative"

    if os.path.exists(
        CSV_PATH
    ):

        df = pd.read_csv(
            CSV_PATH
        )

    else:

        df = pd.DataFrame(
            columns=[
                "prediction"
            ]
        )

    new_row = pd.DataFrame(
        {
            "prediction": [prediction]
        }
    )

    df = pd.concat(
        [df, new_row],
        ignore_index=True
    )

    df.to_csv(
        CSV_PATH,
        index=False
    )

    return render_template(
        "result.html",
        prediction=prediction
    )


@app.route("/dashboard")
def dashboard():

    if not os.path.exists(
        CSV_PATH
    ):

        return "predictions.csv not found"

    df = pd.read_csv(
        CSV_PATH
    )

    if len(df) == 0:

        return "No prediction data available"

    counts = df[
        "prediction"
    ].value_counts()

    plt.figure(
        figsize=(6, 4)
    )

    plt.bar(
        counts.index,
        counts.values
    )

    plt.title(
        "Prediction Counts"
    )

    plt.xlabel(
        "Prediction"
    )

    plt.ylabel(
        "Count"
    )

    plt.tight_layout()

    plt.savefig(
        CHART_PATH
    )

    plt.close()

    return render_template(
        "dashboard.html",
        total_predictions=len(df)
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )