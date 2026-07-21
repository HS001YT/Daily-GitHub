import os

import numpy as np

import matplotlib.pyplot as plt


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OTHER_FILES_DIR = os.path.join(
    BASE_DIR,
    "other_files"
)

os.makedirs(
    OTHER_FILES_DIR,
    exist_ok=True
)

GRAPH_PATH = os.path.join(
    OTHER_FILES_DIR,
    "activation_functions.png"
)


x = np.linspace(
    -10,
    10,
    500
)


relu = np.maximum(
    0,
    x
)

sigmoid = (
    1 /
    (
        1 +
        np.exp(-x)
    )
)

tanh = np.tanh(
    x
)


plt.figure(
    figsize=(10, 6)
)

plt.plot(
    x,
    relu,
    label="ReLU"
)

plt.plot(
    x,
    sigmoid,
    label="Sigmoid"
)

plt.plot(
    x,
    tanh,
    label="Tanh"
)

plt.title(
    "Activation Functions Comparison"
)

plt.xlabel(
    "Input Values"
)

plt.ylabel(
    "Output Values"
)

plt.legend()

plt.grid()


plt.savefig(
    GRAPH_PATH,
    bbox_inches="tight"
)
plt.show()

plt.close()


print(
    "\nGraph Saved Successfully!"
)

print(
    "\nLocation:"
)

print(
    GRAPH_PATH
)