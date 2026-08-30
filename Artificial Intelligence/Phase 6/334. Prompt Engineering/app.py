import os

from dotenv import load_dotenv
from google import genai

from prompts import (
    SYSTEM_PROMPT,
    build_analysis_prompt
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
        "\nGEMINI_API_KEY is not configured.\n\n"
        "Create a .env file in the project folder "
        "and add:\n\n"
        "GEMINI_API_KEY=your_api_key_here"
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

def validate_text(text):
    """
    Validate user input before sending it to the LLM.
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


    minimum_length = 5


    if len(text) < minimum_length:

        raise ValueError(
            "Please enter at least "
            f"{minimum_length} characters."
        )


    maximum_length = 10000


    if len(text) > maximum_length:

        raise ValueError(
            "Text is too long. "
            f"Maximum allowed length is "
            f"{maximum_length} characters."
        )


    return text


# ---------------------------------------------------------
# RESPONSE VALIDATION
# ---------------------------------------------------------

def validate_response(response_text):
    """
    Validate that the AI response follows
    the required structure.
    """

    response_text = response_text.strip()


    if not response_text:

        raise RuntimeError(
            "The AI returned an empty response."
        )


    required_fields = [

        "Topic:",

        "Sentiment:",

        "Complexity:",

        "Summary:",

        "Keywords:"
    ]


    missing_fields = []


    for field in required_fields:

        if field not in response_text:

            missing_fields.append(
                field
            )


    if missing_fields:

        raise RuntimeError(
            "The AI response did not follow "
            "the required format.\n\n"
            "Missing fields: "
            + ", ".join(
                missing_fields
            )
        )


    return response_text


# ---------------------------------------------------------
# EXTRACT RESPONSE DATA
# ---------------------------------------------------------

def parse_response(response_text):
    """
    Convert the AI text response into
    a structured Python dictionary.
    """

    result = {

        "Topic": "",

        "Sentiment": "",

        "Complexity": "",

        "Summary": "",

        "Keywords": ""
    }


    lines = response_text.splitlines()


    current_field = None


    for line in lines:

        line = line.strip()


        if not line:

            continue


        if line.startswith(
            "Topic:"
        ):

            result["Topic"] = (
                line.replace(
                    "Topic:",
                    "",
                    1
                )
                .strip()
            )

            current_field = "Topic"


        elif line.startswith(
            "Sentiment:"
        ):

            result["Sentiment"] = (
                line.replace(
                    "Sentiment:",
                    "",
                    1
                )
                .strip()
            )

            current_field = "Sentiment"


        elif line.startswith(
            "Complexity:"
        ):

            result["Complexity"] = (
                line.replace(
                    "Complexity:",
                    "",
                    1
                )
                .strip()
            )

            current_field = "Complexity"


        elif line.startswith(
            "Summary:"
        ):

            result["Summary"] = (
                line.replace(
                    "Summary:",
                    "",
                    1
                )
                .strip()
            )

            current_field = "Summary"


        elif line.startswith(
            "Keywords:"
        ):

            result["Keywords"] = (
                line.replace(
                    "Keywords:",
                    "",
                    1
                )
                .strip()
            )

            current_field = "Keywords"


        else:

            if current_field:

                result[current_field] += (
                    " "
                    + line
                )


    return result


# ---------------------------------------------------------
# RESULT VALIDATION
# ---------------------------------------------------------

def validate_result(result):
    """
    Validate extracted analysis values.
    """

    for field, value in result.items():

        if not value:

            raise RuntimeError(
                "Unable to extract the "
                f"'{field}' field from "
                "the AI response."
            )


    allowed_sentiments = {

        "Positive",

        "Negative",

        "Neutral"
    }


    sentiment = (
        result["Sentiment"]
        .strip()
        .capitalize()
    )


    if sentiment not in allowed_sentiments:

        result["Sentiment"] = (
            result["Sentiment"]
            + " (Unexpected value)"
        )


    allowed_complexities = {

        "Beginner",

        "Intermediate",

        "Advanced"
    }


    complexity = (
        result["Complexity"]
        .strip()
        .capitalize()
    )


    if complexity not in allowed_complexities:

        result["Complexity"] = (
            result["Complexity"]
            + " (Unexpected value)"
        )


    return result


# ---------------------------------------------------------
# GEMINI REQUEST
# ---------------------------------------------------------

def analyze_text(text):
    """
    Send text to Gemini using:

    - System instructions
    - Few-shot examples
    - Output constraints
    """

    text = validate_text(
        text
    )


    user_prompt = build_analysis_prompt(
        text
    )


    try:

        interaction = (
            client.interactions.create(

                model=MODEL_NAME,

                system_instruction=(
                    SYSTEM_PROMPT
                ),

                input=user_prompt,

                generation_config={
                    "temperature": 0.2
                }
            )
        )


    except Exception as error:

        raise RuntimeError(
            "Gemini API request failed:\n"
            f"{error}"
        ) from error


    response_text = (
        interaction.output_text
    )


    response_text = validate_response(
        response_text
    )


    result = parse_response(
        response_text
    )


    result = validate_result(
        result
    )


    return result


# ---------------------------------------------------------
# DISPLAY RESULT
# ---------------------------------------------------------

def display_result(result):
    """
    Display the AI analysis in a clean format.
    """

    print()

    print("=" * 65)

    print(
        "AI TEXT ANALYSIS RESULT"
    )

    print("=" * 65)


    print()

    print(
        f"Topic:\n"
        f"{result['Topic']}"
    )


    print()

    print(
        f"Sentiment:\n"
        f"{result['Sentiment']}"
    )


    print()

    print(
        f"Complexity:\n"
        f"{result['Complexity']}"
    )


    print()

    print(
        f"Summary:\n"
        f"{result['Summary']}"
    )


    print()

    print(
        f"Keywords:\n"
        f"{result['Keywords']}"
    )


    print()

    print("=" * 65)


# ---------------------------------------------------------
# APPLICATION HEADER
# ---------------------------------------------------------

def display_header():
    """
    Display the application information.
    """

    print()

    print("=" * 65)

    print(
        "DAY 334 — PROMPT ENGINEERING"
    )

    print(
        "Prompt-Based Text Analyzer"
    )

    print("=" * 65)


    print()

    print(
        "This application demonstrates:"
    )


    print(
        "1. System Prompts"
    )


    print(
        "2. Few-Shot Examples"
    )


    print(
        "3. Output Constraints"
    )


    print(
        "4. Temperature Control"
    )


    print()

    print(
        "Enter text to analyze."
    )


    print(
        "Type 'exit' to close "
        "the application."
    )


# ---------------------------------------------------------
# MAIN APPLICATION
# ---------------------------------------------------------

def main():

    display_header()


    while True:

        try:

            print()


            text = input(
                "Text > "
            )


            if (
                text
                .strip()
                .lower()
                == "exit"
            ):

                print()

                print(
                    "Application closed."
                )

                break


            print()

            print(
                "Analyzing text..."
            )


            result = analyze_text(
                text
            )


            display_result(
                result
            )


        except ValueError as error:

            print()

            print(
                "Input Error:"
            )

            print(
                error
            )


        except RuntimeError as error:

            print()

            print(
                "Application Error:"
            )

            print(
                error
            )


        except KeyboardInterrupt:

            print()

            print()

            print(
                "Application interrupted."
            )

            break


        except Exception as error:

            print()

            print(
                "Unexpected Error:"
            )

            print(
                error
            )


# ---------------------------------------------------------
# APPLICATION ENTRY POINT
# ---------------------------------------------------------

if __name__ == "__main__":

    main()