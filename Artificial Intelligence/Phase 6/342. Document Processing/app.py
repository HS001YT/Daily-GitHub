from pathlib import Path

from document_processor import (
    SUPPORTED_EXTENSIONS,
    extract_text
)


BASE_DIR = Path(
    __file__
).resolve().parent

INPUT_DIR = BASE_DIR / "input_documents"

OUTPUT_DIR = BASE_DIR / "processed_documents"

INPUT_DIR.mkdir(
    exist_ok=True
)

OUTPUT_DIR.mkdir(
    exist_ok=True
)


def display_supported_formats():
    print()
    print("Supported formats:")
    print("  TXT")
    print("  PDF")
    print("  DOCX")
    print("  CSV")


def list_documents():
    files = []

    for path in INPUT_DIR.iterdir():

        if (
            path.is_file()
            and path.suffix.lower()
            in SUPPORTED_EXTENSIONS
        ):
            files.append(path)

    return sorted(files)


def display_documents(files):
    print()
    print("=" * 60)
    print("AVAILABLE DOCUMENTS")
    print("=" * 60)

    if not files:
        print()
        print(
            "No supported documents found."
        )
        print(
            f"Add files to: {INPUT_DIR}"
        )
        return

    for index, path in enumerate(
        files,
        start=1
    ):
        print(
            f"{index}. {path.name}"
        )


def save_processed_text(
    file_path,
    text
):
    output_name = (
        file_path.stem
        + "_processed.txt"
    )

    output_path = (
        OUTPUT_DIR
        / output_name
    )

    output_path.write_text(
        text,
        encoding="utf-8"
    )

    return output_path


def process_document(file_path):
    print()
    print(
        f"Processing: {file_path.name}"
    )

    text = extract_text(
        file_path
    )

    if not text:
        print(
            "No text could be extracted."
        )
        return

    output_path = save_processed_text(
        file_path,
        text
    )

    print()
    print(
        "Processing completed."
    )

    print(
        f"Characters extracted: "
        f"{len(text):,}"
    )

    print(
        f"Words extracted: "
        f"{len(text.split()):,}"
    )

    print(
        f"Saved to: {output_path}"
    )

    print()
    print("-" * 60)
    print("EXTRACTED TEXT PREVIEW")
    print("-" * 60)

    preview = text[:2000]

    print(preview)

    if len(text) > 2000:
        print()
        print("... [preview truncated]")


def main():
    print()
    print("=" * 60)
    print("DOCUMENT PROCESSING SYSTEM")
    print("=" * 60)

    display_supported_formats()

    while True:
        files = list_documents()

        display_documents(files)

        if not files:
            print()
            print(
                "Add a document and restart the application."
            )
            return

        print()
        print(
            "Enter the document number to process."
        )
        print(
            "Type 'all' to process every document."
        )
        print(
            "Type 'exit' to close."
        )

        choice = input(
            "\nChoice > "
        ).strip()

        if choice.lower() == "exit":
            print()
            print(
                "Application closed."
            )
            break

        if choice.lower() == "all":

            for file_path in files:

                try:
                    process_document(
                        file_path
                    )

                except Exception as error:
                    print()
                    print(
                        f"Error processing "
                        f"{file_path.name}: {error}"
                    )

            continue

        try:
            index = int(choice) - 1

            if index < 0 or index >= len(files):
                print(
                    "Invalid document number."
                )
                continue

            process_document(
                files[index]
            )

        except ValueError:
            print(
                "Enter a valid number, 'all' or 'exit'."
            )

        except Exception as error:
            print()
            print(
                f"Processing error: {error}"
            )


if __name__ == "__main__":
    main()