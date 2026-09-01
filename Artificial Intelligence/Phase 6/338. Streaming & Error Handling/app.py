import os
import time
from dotenv import load_dotenv
from flask import Flask, Response, render_template, request, stream_with_context
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-3.6-flash"
MAX_RETRIES = 2
RETRY_DELAY = 2

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY not found. Add it to your .env file."
    )

client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

conversation_history = []


def build_prompt(user_message):
    messages = []

    for message in conversation_history:
        messages.append(
            f"{message['role'].title()}: {message['content']}"
        )

    messages.append(f"User: {user_message}")

    return "\n".join(messages)


def get_error_message(error):
    error_text = str(error).lower()

    if "401" in error_text or "authentication" in error_text:
        return "API key is invalid or missing."

    if "403" in error_text or "permission" in error_text:
        return "API access was denied."

    if "404" in error_text or "not found" in error_text:
        return "The selected AI model is unavailable."

    if "429" in error_text or "rate" in error_text:
        return "Too many requests. Please wait and try again."

    if "timeout" in error_text:
        return "The AI request took too long. Please try again."

    if "503" in error_text or "unavailable" in error_text:
        return "The AI service is temporarily unavailable."

    return "Unable to generate a response. Please try again."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not data:
        return {"error": "Invalid request."}, 400

    user_message = data.get("message", "").strip()

    if not user_message:
        return {"error": "Please enter a message."}, 400

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    prompt = build_prompt(user_message)

    def generate_response():
        response_text = ""

        for attempt in range(MAX_RETRIES + 1):
            try:
                stream = client.interactions.create(
                    model=MODEL_NAME,
                    input=prompt,
                    stream=True
                )

                for event in stream:
                    if (
                        event.event_type == "step.delta"
                        and event.delta
                        and event.delta.type == "text"
                    ):
                        chunk = event.delta.text

                        if chunk:
                            response_text += chunk
                            yield chunk

                if response_text:
                    conversation_history.append({
                        "role": "assistant",
                        "content": response_text
                    })

                return

            except Exception as error:
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY * (attempt + 1))
                    continue

                error_message = get_error_message(error)

                yield f"\n\n[Error: {error_message}]"

                return

    return Response(
        stream_with_context(generate_response()),
        content_type="text/plain"
    )


@app.route("/clear", methods=["POST"])
def clear_chat():
    conversation_history.clear()

    return {
        "message": "Conversation cleared successfully."
    }


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )