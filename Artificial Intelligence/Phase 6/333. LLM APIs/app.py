import json
import os

from dotenv import load_dotenv
from openai import OpenAI


# ---------------------------------------------------------
# Environment Configuration
# ---------------------------------------------------------

load_dotenv()


API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = os.getenv(
    "OPENAI_MODEL",
    "gpt-5.6-luna"
)


# ---------------------------------------------------------
# Validation
# ---------------------------------------------------------

if not API_KEY:

    raise RuntimeError(
        "OPENAI_API_KEY is not configured.\n"
        "Create a .env file and add:\n"
        "OPENAI_API_KEY=your_api_key_here"
    )


# ---------------------------------------------------------
# OpenAI Client
# ---------------------------------------------------------

client = OpenAI(
    api_key=API_KEY
)


# ---------------------------------------------------------
# Prompt Configuration
# ---------------------------------------------------------

SYSTEM_PROMPT = """
You are an information extraction assistant.

Analyze the text provided by the user.

Return ONLY valid JSON.

The JSON should contain these fields:

{
    "topic": "main topic of the text",
    "category": "general category",
    "summary": "short summary",
    "keywords": [
        "keyword1",
        "keyword2",
        "keyword3"
    ]
}

Do not include Markdown.
Do not include code fences.
Do not include explanations outside the JSON.
"""


# ---------------------------------------------------------
# Input Validation
# ---------------------------------------------------------

def validate_text(text):
    """
    Validate the user's input.
    """

    if text is None:

        raise ValueError(
            "Text cannot be empty."
        )


    text = text.strip()


    if not text:

        raise ValueError(
            "Text cannot be empty."
        )


    if len(text) > 10000:

        raise ValueError(
            "Text is too long. "
            "Maximum allowed length is 10,000 characters."
        )


    return text


# ---------------------------------------------------------
# LLM Request
# ---------------------------------------------------------

def analyze_text(text):
    """
    Send text to the LLM and return
    the generated structured response.
    """

    text = validate_text(
        text
    )


    user_prompt = (
        "Analyze the following text:\n\n"
        f"{text}"
    )


    try:

        response = client.responses.create(

            model=MODEL_NAME,

            instructions=SYSTEM_PROMPT,

            input=user_prompt,

            temperature=0.2
        )


    except Exception as error:

        raise RuntimeError(
            f"LLM API request failed: {error}"
        ) from error


    content = response.output_text


    if not content:

        raise RuntimeError(
            "The LLM returned an empty response."
        )


    return parse_response(
        content
    )


# ---------------------------------------------------------
# Response Parsing
# ---------------------------------------------------------

def parse_response(content):
    """
    Convert the LLM response into a Python dictionary.
    """

    content = content.strip()


    try:

        result = json.loads(
            content
        )


    except json.JSONDecodeError:

        # Sometimes a model may still return
        # Markdown code fences despite instructions.

        cleaned_content = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )


        try:

            result = json.loads(
                cleaned_content
            )

        except json.JSONDecodeError as error:

            raise RuntimeError(
                "The LLM response was not valid JSON.\n\n"
                f"Raw response:\n{content}"
            ) from error


    if not isinstance(
        result,
        dict
    ):

        raise RuntimeError(
            "The LLM returned JSON, "
            "but it was not a JSON object."
        )


    return result


# ---------------------------------------------------------
# Result Display
# ---------------------------------------------------------

def display_result(result):
    """
    Display the structured AI response.
    """

    print()
    print("=" * 60)
    print("AI ANALYSIS")
    print("=" * 60)


    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )


    print("=" * 60)


# ---------------------------------------------------------
# Main Application
# ---------------------------------------------------------

def main():

    print()
    print("=" * 60)
    print("AI PROMPT ANALYZER")
    print("=" * 60)

    print(
        "\nEnter text for the LLM to analyze."
    )

    print(
        "Type 'exit' to close the application."
    )


    while True:

        print()

        text = input(
            "Text > "
        )


        if text.strip().lower() == "exit":

            print(
                "\nApplication closed."
            )

            break


        try:

            result = analyze_text(
                text
            )


            display_result(
                result
            )


        except ValueError as error:

            print(
                f"\nInput Error: {error}"
            )


        except RuntimeError as error:

            print(
                f"\nApplication Error: {error}"
            )


        except KeyboardInterrupt:

            print(
                "\n\nApplication interrupted."
            )

            break


# ---------------------------------------------------------
# Application Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":

    main()