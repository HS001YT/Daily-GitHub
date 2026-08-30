import os

from flask import (
    Flask,
    jsonify,
    render_template,
    request
)

from ai_service import generate_response


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


app = Flask(__name__)


app.config["MAX_CONTENT_LENGTH"] = (
    1 * 1024 * 1024
)


# ---------------------------------------------------------
# HOME ROUTE
# ---------------------------------------------------------

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ---------------------------------------------------------
# CHAT API
# ---------------------------------------------------------

@app.route(
    "/api/chat",
    methods=["POST"]
)
def chat():

    try:

        data = request.get_json()


        if not data:

            return jsonify(
                {
                    "success": False,
                    "error": (
                        "Invalid request data."
                    )
                }
            ), 400


        message = data.get(
            "message",
            ""
        )


        if not isinstance(
            message,
            str
        ):

            return jsonify(
                {
                    "success": False,
                    "error": (
                        "Message must be text."
                    )
                }
            ), 400


        message = message.strip()


        if not message:

            return jsonify(
                {
                    "success": False,
                    "error": (
                        "Please enter a message."
                    )
                }
            ), 400


        maximum_length = 10000


        if len(message) > maximum_length:

            return jsonify(
                {
                    "success": False,
                    "error": (
                        "Message is too long. "
                        f"Maximum allowed length is "
                        f"{maximum_length} characters."
                    )
                }
            ), 400


        response = generate_response(
            message
        )


        return jsonify(
            {
                "success": True,
                "response": response
            }
        )


    except RuntimeError as error:

        return jsonify(
            {
                "success": False,
                "error": str(error)
            }
        ), 500


    except Exception as error:

        print(
            f"Unexpected server error: "
            f"{error}"
        )


        return jsonify(
            {
                "success": False,
                "error": (
                    "An unexpected error occurred."
                )
            }
        ), 500


# ---------------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print(
        "DAY 336 — FLASK + LLM"
    )

    print(
        "AI CHATBOT"
    )

    print("=" * 60)

    print()

    print(
        "Open in Chrome:"
    )

    print(
        "http://127.0.0.1:5000"
    )

    print()


    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )