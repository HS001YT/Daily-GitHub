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
    "gemini-3.7-flash"
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

Follow these rules:

1. Answer clearly and accurately.
2. Be helpful and friendly.
3. Explain concepts when the user asks questions.
4. Do not claim to perform actions you cannot perform.
5. If you are uncertain, say so clearly.
6. Keep answers appropriately concise unless the user
   requests detailed information.
7. Use examples when they help understanding.
"""


# ---------------------------------------------------------
# MESSAGE VALIDATION
# ---------------------------------------------------------

def validate_message(message):

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


    maximum_length = 10000


    if len(message) > maximum_length:

        raise ValueError(
            "Message exceeds the maximum allowed length."
        )


    return message


# ---------------------------------------------------------
# GENERATE AI RESPONSE
# ---------------------------------------------------------

def generate_response(message):

    message = validate_message(
        message
    )


    prompt = f"""
{SYSTEM_INSTRUCTION}

User message:

{message}

Respond directly to the user's message.
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