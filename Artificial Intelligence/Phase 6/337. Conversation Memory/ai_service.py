import os

from dotenv import load_dotenv
from google import genai


# ---------------------------------------------------------
# ENVIRONMENT CONFIGURATION
# ---------------------------------------------------------

load_dotenv()


API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash"
)


# ---------------------------------------------------------
# API KEY VALIDATION
# ---------------------------------------------------------

if not API_KEY:

    raise RuntimeError(
        "GEMINI_API_KEY was not found. "
        "Check your .env file."
    )


# ---------------------------------------------------------
# GEMINI CLIENT
# ---------------------------------------------------------

client = genai.Client(
    api_key=API_KEY
)


# ---------------------------------------------------------
# SYSTEM INSTRUCTION
# ---------------------------------------------------------

SYSTEM_INSTRUCTION = """
You are a helpful AI chatbot.

You receive conversation history along with the
latest user message.

Use previous messages when they are relevant to the
current question.

Do not pretend to remember information that is not
included in the conversation history.

Follow these rules:

1. Answer clearly and accurately.
2. Be helpful and friendly.
3. Use previous conversation context when relevant.
4. Explain concepts when requested.
5. If uncertain, say so clearly.
6. Keep answers concise unless the user requests
   detailed information.
"""


# ---------------------------------------------------------
# MESSAGE VALIDATION
# ---------------------------------------------------------

def validate_message(
    message
):

    if message is None:

        raise ValueError(
            "Message cannot be empty."
        )


    if not isinstance(
        message,
        str
    ):

        raise ValueError(
            "Message must be text."
        )


    message = message.strip()


    if not message:

        raise ValueError(
            "Message cannot be empty."
        )


    return message


# ---------------------------------------------------------
# FORMAT CONVERSATION
# ---------------------------------------------------------

def format_conversation(
    history
):

    formatted_history = []


    for message in history:

        role = message.get(
            "role",
            ""
        )


        content = message.get(
            "content",
            ""
        )


        if not content:

            continue


        if role == "user":

            formatted_history.append(
                f"User: {content}"
            )


        elif role == "assistant":

            formatted_history.append(
                f"Assistant: {content}"
            )


    return "\n".join(
        formatted_history
    )


# ---------------------------------------------------------
# GENERATE RESPONSE
# ---------------------------------------------------------

def generate_response(
    message,
    history=None
):

    message = validate_message(
        message
    )


    if history is None:

        history = []


    conversation_text = (
        format_conversation(
            history
        )
    )


    prompt = f"""
{SYSTEM_INSTRUCTION}

Conversation history:

{conversation_text}

Latest user message:

User: {message}

Respond directly to the latest user message.
"""


    try:

        response = (
            client.models.generate_content(

                model=MODEL_NAME,

                contents=prompt
            )
        )


        response_text = (
            response.text
        )


        if not response_text:

            raise RuntimeError(
                "The AI returned an empty response."
            )


        return response_text.strip()


    except Exception as error:

        raise RuntimeError(
            "Gemini API request failed: "
            f"{error}"
        ) from error