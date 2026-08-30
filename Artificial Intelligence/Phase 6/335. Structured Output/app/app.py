import json

from extractor import (
    extract_information
)


# ---------------------------------------------------------
# APPLICATION HEADER
# ---------------------------------------------------------

def display_header():

    print()

    print("=" * 65)

    print(
        "DAY 335 — STRUCTURED OUTPUT"
    )

    print(
        "AI INFORMATION EXTRACTOR"
    )

    print("=" * 65)


    print()

    print(
        "Enter unstructured text and the AI will"
    )

    print(
        "extract structured information as JSON."
    )


    print()

    print(
        "Type 'exit' to close the application."
    )


# ---------------------------------------------------------
# DISPLAY JSON RESULT
# ---------------------------------------------------------

def display_result(data):

    print()

    print("=" * 65)

    print(
        "EXTRACTED INFORMATION"
    )

    print("=" * 65)


    print()


    json_data = (
        data.model_dump()
    )


    formatted_json = json.dumps(

        json_data,

        indent=4,

        ensure_ascii=False
    )


    print(
        formatted_json
    )


    print()

    print("=" * 65)


# ---------------------------------------------------------
# MULTILINE INPUT
# ---------------------------------------------------------

def get_user_input():

    print()

    print(
        "Enter your text."
    )

    print(
        "Press Enter on an empty line to analyze."
    )


    lines = []


    while True:

        try:

            line = input()


            if not line.strip():

                break


            lines.append(
                line
            )


        except EOFError:

            break


    return "\n".join(
        lines
    )


# ---------------------------------------------------------
# MAIN APPLICATION
# ---------------------------------------------------------

def main():

    display_header()


    while True:

        try:

            print()

            print(
                "-" * 65
            )


            print(
                "TEXT INPUT"
            )


            print(
                "-" * 65
            )


            text = get_user_input()


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


            if not text.strip():

                print()

                print(
                    "Input Error:"
                )

                print(
                    "No text was entered."
                )

                continue


            print()

            print(
                "Extracting information..."
            )


            result = (
                extract_information(
                    text
                )
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