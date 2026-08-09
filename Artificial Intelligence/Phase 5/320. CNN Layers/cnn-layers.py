import os

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Input,
    Conv2D,
    MaxPooling2D,
    Flatten
)

from tensorflow.keras.datasets import mnist


# ==========================================================
# Configuration
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "output"
)

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


print("=" * 70)
print("CNN LAYERS DEMONSTRATION")
print("=" * 70)

print()


# ==========================================================
# Load MNIST Image
# ==========================================================

print("Loading MNIST dataset...")

(X_train, y_train), _ = mnist.load_data()

image = X_train[0]

label = y_train[0]

print()

print("Image Label :", label)

print("Original Shape :", image.shape)

print()


# ==========================================================
# Normalize Image
# ==========================================================

image = image.astype(
    "float32"
) / 255.0


# ==========================================================
# Reshape Image
# ==========================================================

image = image.reshape(
    1,
    28,
    28,
    1
)

print("CNN Input Shape :", image.shape)

print()


# ==========================================================
# Create Convolution Layer
# ==========================================================

conv_layer = Conv2D(

    filters=32,

    kernel_size=(3, 3),

    activation="relu"

)


# ==========================================================
# Apply Convolution
# ==========================================================

convolution_output = conv_layer(

    image

)

print("=" * 70)

print("CONVOLUTION")

print("=" * 70)

print()

print(

    "Input Shape :",

    image.shape

)

print(

    "Output Shape :",

    convolution_output.shape

)

print()


# ==========================================================
# Create Pooling Layer
# ==========================================================

pooling_layer = MaxPooling2D(

    pool_size=(2, 2)

)


# ==========================================================
# Apply Pooling
# ==========================================================

pooling_output = pooling_layer(

    convolution_output

)

print("=" * 70)

print("MAX POOLING")

print("=" * 70)

print()

print(

    "Input Shape :",

    convolution_output.shape

)

print(

    "Output Shape :",

    pooling_output.shape

)

print()


# ==========================================================
# Flatten Layer
# ==========================================================

flatten_layer = Flatten()

flatten_output = flatten_layer(

    pooling_output

)

print("=" * 70)

print("FLATTEN")

print("=" * 70)

print()

print(

    "Input Shape :",

    pooling_output.shape

)

print(

    "Output Shape :",

    flatten_output.shape

)

print()


# ==========================================================
# Build Complete CNN Pipeline
# ==========================================================

model = Sequential(

    [

        Input(

            shape=(28, 28, 1)

        ),

        Conv2D(

            32,

            (3, 3),

            activation="relu"

        ),

        MaxPooling2D(

            (2, 2)

        ),

        Flatten()

    ]

)


print("=" * 70)

print("COMPLETE CNN PIPELINE")

print("=" * 70)

print()

model.summary()

print()


# ==========================================================
# Visualize Original Image
# ==========================================================

plt.figure(

    figsize=(5, 5)

)

plt.imshow(

    image[0, :, :, 0],

    cmap="gray"

)

plt.title(

    f"Original Image - Digit {label}"

)

plt.axis("off")

plt.tight_layout()

plt.savefig(

    os.path.join(

        OUTPUT_DIR,

        "original_image.png"

    ),

    dpi=300,

    bbox_inches="tight"

)

plt.close()


# ==========================================================
# Visualize Convolution Feature Maps
# ==========================================================

plt.figure(

    figsize=(12, 8)

)

for i in range(9):

    plt.subplot(

        3,

        3,

        i + 1

    )

    plt.imshow(

        convolution_output[0, :, :, i],

        cmap="gray"

    )

    plt.title(

        f"Filter {i + 1}"

    )

    plt.axis("off")

plt.tight_layout()

plt.savefig(

    os.path.join(

        OUTPUT_DIR,

        "convolution_feature_maps.png"

    ),

    dpi=300,

    bbox_inches="tight"

)

plt.close()


# ==========================================================
# Visualize Pooling Output
# ==========================================================

plt.figure(

    figsize=(12, 8)

)

for i in range(9):

    plt.subplot(

        3,

        3,

        i + 1

    )

    plt.imshow(

        pooling_output[0, :, :, i],

        cmap="gray"

    )

    plt.title(

        f"Pooled Map {i + 1}"

    )

    plt.axis("off")

plt.tight_layout()

plt.savefig(

    os.path.join(

        OUTPUT_DIR,

        "pooling_feature_maps.png"

    ),

    dpi=300,

    bbox_inches="tight"

)

plt.close()


# ==========================================================
# Final Information
# ==========================================================

print("=" * 70)

print("CNN LAYER FLOW")

print("=" * 70)

print()

print("Original Image")

print("28 × 28 × 1")

print()

print("        ↓")

print()

print("Conv2D")

print("26 × 26 × 32")

print()

print("        ↓")

print()

print("MaxPooling2D")

print("13 × 13 × 32")

print()

print("        ↓")

print()

print("Flatten")

print("5408 values")

print()

print("=" * 70)

print("OUTPUT FILES")

print("=" * 70)

print()

print("original_image.png")

print("convolution_feature_maps.png")

print("pooling_feature_maps.png")

print()

print("=" * 70)

print("CNN LAYERS DEMONSTRATION COMPLETED")

print("=" * 70)