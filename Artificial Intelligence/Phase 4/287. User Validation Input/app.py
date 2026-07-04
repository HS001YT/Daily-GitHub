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
    "/predict",
    methods=["POST"]
)
def predict():

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

        if glucose > 140:

            result = (
                "High Glucose Level Detected"
            )

        else:

            result = (
                "Normal Glucose Level"
            )

        return render_template(
            "result.html",
            success=True,
            result=result
        )

    except ValueError as error:

        return render_template(
            "result.html",
            success=False,
            result=str(error)
        )

    except Exception as error:

        return render_template(
            "result.html",
            success=False,
            result=f"Unexpected Error: {error}"
        )


if __name__ == "__main__":

    app.run(
        debug=True
    )