import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

import numpy as np


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


prediction = model.predict(
    np.array(
        [7],
        dtype=np.float32
    ),
    verbose=0
)


model.save(
    os.path.join(
        OTHER_FILES_DIR,
        "training_model.keras"
    )
)


print(
    "\nPrediction For 7:"
)

print(
    round(
        float(
            prediction[0][0]
        ),
        2
    )
)

print(
    "\nFinal Loss:"
)

print(
    history.history["loss"][-1]
)