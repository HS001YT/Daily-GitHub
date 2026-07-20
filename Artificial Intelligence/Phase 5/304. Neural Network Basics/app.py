import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
import numpy as np


study_hours = np.array(
    [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
    ],
    dtype=np.float32
)

marks = np.array(
    [
        10,
        20,
        30,
        40,
        50,
        60,
        70,
        80
    ],
    dtype=np.float32
)


model = tf.keras.Sequential(
    [
        tf.keras.Input(
            shape=(1,)
        ),

        tf.keras.layers.Dense(
            units=1
        )
    ]
)


model.compile(
    optimizer=tf.keras.optimizers.SGD(
        learning_rate=0.01
    ),
    loss="mean_squared_error"
)


history = model.fit(
    study_hours,
    marks,
    epochs=3000,
    verbose=0
)


prediction = model.predict(
    np.array(
        [9],
        dtype=np.float32
    ),
    verbose=0
)


print(
    "\nPrediction for 9 Study Hours:"
)

print(
    round(
        float(
            prediction[0][0]
        ),
        2
    )
)


weights = model.layers[0].get_weights()

print(
    "\nLearned Weights and Bias:"
)

print(
    weights
)


print(
    "\nFinal Loss:"
)

print(
    history.history["loss"][-1]
)