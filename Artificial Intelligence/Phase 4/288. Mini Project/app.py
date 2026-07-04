from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    try:

        age = float(
            request.form.get(
                "age"
            )
        )

        bmi = float(
            request.form.get(
                "bmi"
            )
        )

        glucose = float(
            request.form.get(
                "glucose"
            )
        )

        if age < 1 or age > 120:

            raise ValueError(
                "Age must be between 1 and 120."
            )

        if bmi < 10 or bmi > 80:

            raise ValueError(
                "BMI must be between 10 and 80."
            )

        if glucose < 50 or glucose > 500:

            raise ValueError(
                "Glucose must be between 50 and 500."
            )

        risk_score = 0

        if age > 50:

            risk_score += 1

        if bmi > 30:

            risk_score += 1

        if glucose > 140:

            risk_score += 1

        if risk_score == 0:

            risk_level = "Low Risk"

            recommendation = (
                "Maintain your current healthy lifestyle."
            )

        elif risk_score == 1:

            risk_level = "Moderate Risk"

            recommendation = (
                "Monitor health regularly and improve diet."
            )

        elif risk_score == 2:

            risk_level = "High Risk"

            recommendation = (
                "Consult a healthcare professional."
            )

        else:

            risk_level = "Very High Risk"

            recommendation = (
                "Medical consultation is strongly recommended."
            )

        return render_template(
            "result.html",
            risk_level=risk_level,
            recommendation=recommendation,
            risk_score=risk_score,
            error=False
        )

    except Exception as error:

        return render_template(
            "result.html",
            error=True,
            message=str(error)
        )


if __name__ == "__main__":

    app.run(
        debug=True
    )