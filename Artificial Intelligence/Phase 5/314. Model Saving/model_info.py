import json
import os


# ==========================================================
# Paths
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)

METADATA_PATH = os.path.join(
    OTHER_FILES,
    "metadata.json"
)


# ==========================================================
# Check Metadata File
# ==========================================================

if not os.path.exists(METADATA_PATH):

    print()

    print("=" * 60)

    print("ERROR")

    print("=" * 60)

    print()

    print("metadata.json not found.")

    print("Run generate_metadata.py first.")

    exit()


# ==========================================================
# Load Metadata
# ==========================================================

with open(
    METADATA_PATH,
    "r"
) as file:

    metadata = json.load(file)


# ==========================================================
# Display Model Information
# ==========================================================

print()

print("=" * 60)

print("DEEP LEARNING MODEL INFORMATION")

print("=" * 60)

print()

print(f"Model Name       : {metadata['model_name']}")

print(f"Version          : {metadata['version']}")

print(f"Framework        : {metadata['framework']}")

print(f"Dataset          : {metadata['dataset']}")

print(f"Problem Type     : {metadata['problem_type']}")

print(f"Best Accuracy    : {metadata['accuracy']} %")

print(f"Best Loss        : {metadata['loss']}")

print(f"Training Epochs  : {metadata['epochs']}")

print(f"Created On       : {metadata['created_on']}")

print()

print("=" * 60)