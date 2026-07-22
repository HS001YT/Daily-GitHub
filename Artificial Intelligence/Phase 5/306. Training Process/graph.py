import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

import numpy as np

import matplotlib.pyplot as plt


x_train = np.array(
    [
        1,
        2,
        3,
        4,
        5,
        6
    ],
    dtype=np.float32
)

y_train = np.array(
    [
        10,
        20,
        30,
        40,
        50,
        60
    ],
    dtype=np.float32
)


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


model = tf.keras.Sequential(
    [
        tf.keras.Input(
            shape=(1,)
        ),

        tf.keras.layers.Dense(
            1
        )
    ]
)


model.compile(
    optimizer="sgd",
    loss="mse"
)


history = model.fit(
    x_train,
    y_train,
    epochs=500,
    verbose=0
)


plt.figure(
    figsize=(10, 6)
)

plt.plot(
    history.history["loss"]
)

plt.title(
    "Loss Curve"
)

plt.xlabel(
    "Epoch"
)

plt.ylabel(
    "Loss"
)

plt.grid()


SAVE_PATH = os.path.join(
    OTHER_FILES_DIR,
    "loss_curve.png"
)

plt.savefig(
    SAVE_PATH,
    bbox_inches="tight"
)

print(
    "\nGraph Saved:"
)

print(
    SAVE_PATH
)

plt.show()

plt.close()