import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY not found in .env"
    )

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-embedding-001"


def generate_embedding(text):
    text = text.strip()

    if not text:
        raise ValueError(
            "Text cannot be empty."
        )

    response = client.models.embed_content(
        model=MODEL_NAME,
        contents=text
    )

    return response.embeddings[0].values


def generate_embeddings(texts):
    embeddings = []

    for text in texts:
        embeddings.append(
            generate_embedding(text)
        )

    return embeddings