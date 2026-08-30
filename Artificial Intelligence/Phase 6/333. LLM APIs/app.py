import json
import os

from dotenv import load_dotenv
from google import genai


# ---------------------------------------------------------
# Environment Configuration
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
# API Key Validation
# ---------------------------------------------------------

if not API_KEY:

    raise RuntimeError(
        "GEMINI_API_KEY is not configured.\n"
        "Create a .env file and add:\n"
        "GEMINI_API_KEY=your_api_key_here"
    )


# ---------------------------------------------------------
# Gemini Client
# ---------------------------------------------------------

client = genai.Client(
    api_key=API_KEY
)


# ---------------------------------------------------------
# System Instructions
# ---------------------------------------------------------

SYSTEM_PROMPT = """
You are an information extraction assistant.

Analyze the text provided by the user.

Return ONLY valid JSON.

The JSON must contain these fields:

{
    "topic": "main topic of the text",
    "category": "general category",
    "summary": "short summary of the text",
    "keywords": [
        "keyword1",
        "keyword2",
        "keyword3"
    ]
}

Rules:

1. Return only JSON.
2. Do not use Markdown.
3. Do not use code fences.
4. Do not add explanations outside JSON.
5. Keep the summary concise.
6. Extract relevant keywords.
"""


# ---------------------------------------------------------
# Input Validation
# ---------------------------------------------------------

def validate_text(text):

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
            "Maximum allowed length is "
            "10,000 characters."
        )


    return text


# ---------------------------------------------------------
# Response Parsing
# ---------------------------------------------------------

def parse_response(content):

    content = content.strip()


    try:

        result = json.loads(
            content
        )


    except json.JSONDecodeError:

        cleaned_content = (
            content
            .replace(
                "```json",
                ""
            )
            .replace(
                "```",
                ""
            )
            .strip()
        )


        try:

            result = json.loads(
                cleaned_content
            )


        except json.JSONDecodeError as error:

            raise RuntimeError(
                "The AI response was not "
                "valid JSON.\n\n"
                f"Raw response:\n{content}"
            ) from error


    if not isinstance(
        result,
        dict
    ):

        raise RuntimeError(
            "The AI returned JSON, "
            "but it was not a JSON object."
        )


    return result


# ---------------------------------------------------------
# LLM Request
# ---------------------------------------------------------

def analyze_text(text):

    text = validate_text(
        text
    )


    user_prompt = (
        "Analyze the following text:\n\n"
        f"{text}"
    )


    try:

        interaction = (
            client.interactions.create(

                model=MODEL_NAME,

                system_instruction=SYSTEM_PROMPT,

                input=user_prompt
            )
        )


    except Exception as error:

        raise RuntimeError(
            "Gemini API request failed: "
            f"{error}"
        ) from error


    content = interaction.output_text


    if not content:

        raise RuntimeError(
            "The Gemini model returned "
            "an empty response."
        )


    return parse_response(
        content
    )


# ---------------------------------------------------------
# Result Display
# ---------------------------------------------------------

def display_result(result):

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
        "\nEnter text for the AI "
        "to analyze."
    )


    print(
        "Type 'exit' to close "
        "the application."
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