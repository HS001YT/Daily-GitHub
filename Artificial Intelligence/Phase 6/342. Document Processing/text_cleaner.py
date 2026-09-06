import re


def normalize_whitespace(text):
    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    text = re.sub(
        r"\n\s*\n+",
        "\n\n",
        text
    )

    return text.strip()


def remove_empty_lines(text):
    lines = []

    for line in text.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)


def clean_text(text):
    if not isinstance(text, str):
        text = str(text)

    text = text.replace(
        "\x00",
        ""
    )

    text = normalize_whitespace(
        text
    )

    text = remove_empty_lines(
        text
    )

    return text.strip()