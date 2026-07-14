from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def home():

    return """
    <h1>Prediction API</h1>

    <p>Example:</p>

    <a href="/predict?text=This product is good">
        Test Positive Example
    </a>

    <br><br>

    <a href="/predict?text=Worst service ever">
        Test Negative Example
    </a>
    """


@app.route(
    "/predict",
    methods=["GET", "POST"]
)
def predict():

    try:

        if request.method == "GET":

            text = request.args.get(
                "text"
            )

        else:

            data = request.get_json()

            text = data.get(
                "text"
            )

        if not text:

            return jsonify(
                {
                    "error":
                    "Text is required"
                }
            )

        if "good" in text.lower():

            prediction = "Positive"

        else:

            prediction = "Negative"

        return jsonify(
            {
                "input": text,
                "prediction": prediction
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