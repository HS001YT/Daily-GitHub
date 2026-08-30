import os

from dotenv import load_dotenv
from google import genai

from schemas import (
    PersonInformation
)


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
        "\nGEMINI_API_KEY was not found.\n\n"
        "Create a .env file and add:\n\n"
        "GEMINI_API_KEY=your_api_key"
    )


# ---------------------------------------------------------
# GEMINI CLIENT
# ---------------------------------------------------------

client = genai.Client(
    api_key=API_KEY
)


# ---------------------------------------------------------
# INPUT VALIDATION
# ---------------------------------------------------------

def validate_input(text):

    if text is None:

        raise ValueError(
            "Input text cannot be empty."
        )


    text = text.strip()


    if not text:

        raise ValueError(
            "Input text cannot be empty."
        )


    minimum_length = 10


    if len(text) < minimum_length:

        raise ValueError(
            "Please enter at least "
            f"{minimum_length} characters."
        )


    maximum_length = 20000


    if len(text) > maximum_length:

        raise ValueError(
            "Input text is too long.\n"
            f"Maximum allowed length: "
            f"{maximum_length} characters."
        )


    return text


# ---------------------------------------------------------
# PROMPT BUILDER
# ---------------------------------------------------------

def build_prompt(text):

    prompt = f"""
You are an AI information extraction system.

Extract only information that is explicitly stated
or clearly supported by the provided text.

Important rules:

1. Do not invent information.
2. Do not guess missing values.
3. Use null for missing single values.
4. Use an empty list for missing list values.
5. Keep skills specific.
6. Extract organizations separately when possible.
7. The summary must be based only on the input.
8. Return information according to the provided schema.

TEXT TO ANALYZE:

{text}
"""

    return prompt


# ---------------------------------------------------------
# INFORMATION EXTRACTION
# ---------------------------------------------------------

def extract_information(text):

    text = validate_input(
        text
    )


    prompt = build_prompt(
        text
    )


    try:

        response = (
            client.models.generate_content(

                model=MODEL_NAME,

                contents=prompt,

                config={

                    "response_mime_type":
                    "application/json",

                    "response_schema":
                    PersonInformation

                }
            )
        )


    except Exception as error:

        raise RuntimeError(
            "Gemini API request failed:\n"
            f"{error}"
        ) from error


    try:

        if response.parsed is not None:

            extracted_data = (
                response.parsed
            )


        else:

            extracted_data = (
                PersonInformation
                .model_validate_json(
                    response.text
                )
            )


    except Exception as error:

        raise RuntimeError(
            "AI response validation failed:\n"
            f"{error}"
        ) from error


    return extracted_data