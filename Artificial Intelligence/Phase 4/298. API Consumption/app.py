from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

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

        data = request.get_json()

        text = data.get(
            "text"
        )

        if not text:

            return jsonify(
                {
                    "error":
                    "Please enter text"
                }
            )

        if "good" in text.lower():

            prediction = "Positive"

        else:

            prediction = "Negative"

        return jsonify(
            {
                "prediction":
                prediction
            }
        )

    except Exception as error:

        return jsonify(
            {
                "error":
                str(error)
            }
        )


if __name__ == "__main__":

    app.run(
        debug=True
    )