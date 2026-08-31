import os
import uuid

from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    session
)

from ai_service import (
    generate_response
)

from memory import (
    add_message,
    clear_conversation,
    get_conversation,
    get_memory_count
)


# ---------------------------------------------------------
# BASE DIRECTORY
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# ---------------------------------------------------------
# FLASK APPLICATION
# ---------------------------------------------------------

app = Flask(__name__)


# ---------------------------------------------------------
# SECURITY CONFIGURATION
# ---------------------------------------------------------

app.secret_key = os.getenv(
    "FLASK_SECRET_KEY",
    "development-secret-key"
)


app.config[
    "MAX_CONTENT_LENGTH"
] = 1 * 1024 * 1024


# ---------------------------------------------------------
# GET SESSION ID
# ---------------------------------------------------------

def get_session_id():

    if "conversation_id" not in session:

        session[
            "conversation_id"
        ] = uuid.uuid4().hex


    return session[
        "conversation_id"
    ]


# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

@app.route("/")
def home():

    get_session_id()


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
                    "error":
                        "Invalid request data."
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
                    "error":
                        "Message must be text."
                }
            ), 400


        message = message.strip()


        if not message:

            return jsonify(
                {
                    "success": False,
                    "error":
                        "Please enter a message."
                }
            ), 400


        if len(message) > 10000:

            return jsonify(
                {
                    "success": False,
                    "error":
                        "Message is too long."
                }
            ), 400


        session_id = (
            get_session_id()
        )


        history = (
            get_conversation(
                session_id
            )
        )


        response = generate_response(
            message=message,
            history=history
        )


        # Save user message

        add_message(
            session_id,
            "user",
            message
        )


        # Save AI response

        add_message(
            session_id,
            "assistant",
            response
        )


        return jsonify(
            {
                "success": True,
                "response": response,
                "memory_count":
                    get_memory_count(
                        session_id
                    )
            }
        )


    except ValueError as error:

        return jsonify(
            {
                "success": False,
                "error": str(error)
            }
        ), 400


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
                "error":
                    "An unexpected error occurred."
            }
        ), 500


# ---------------------------------------------------------
# GET MEMORY STATUS
# ---------------------------------------------------------

@app.route(
    "/api/memory",
    methods=["GET"]
)
def memory_status():

    session_id = (
        get_session_id()
    )


    count = (
        get_memory_count(
            session_id
        )
    )


    return jsonify(
        {
            "success": True,
            "memory_count": count
        }
    )


# ---------------------------------------------------------
# CLEAR MEMORY
# ---------------------------------------------------------

@app.route(
    "/api/clear-memory",
    methods=["POST"]
)
def clear_memory():

    session_id = (
        get_session_id()
    )


    clear_conversation(
        session_id
    )


    return jsonify(
        {
            "success": True,
            "message":
                "Conversation memory cleared.",
            "memory_count": 0
        }
    )


# ---------------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print(
        "DAY 337 — CONVERSATION MEMORY"
    )

    print(
        "AI CHATBOT WITH MEMORY"
    )

    print("=" * 60)

    print()

    print(
        "Open:"
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