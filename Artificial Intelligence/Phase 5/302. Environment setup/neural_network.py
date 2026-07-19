import tensorflow as tf
import numpy as np


x_train = np.array(
    [1,2,3,4,5,6],
    dtype=float
)

y_train = np.array(
    [2,4,6,8,10,12],
    dtype=float
)


model = tf.keras.Sequential(
    [
        tf.keras.Input(shape=(1,)),
        tf.keras.layers.Dense(1)
    ]
)

model.compile(
    optimizer=tf.keras.optimizers.SGD(
        learning_rate=0.1
    ),
    loss="mse"
)

model.fit(
    x_train,
    y_train,
    epochs=3000,
    verbose=0
)


prediction = model.predict(
    np.array([7.0]),
    verbose=0
)

print(
    "Prediction for 7:"
)

print(
    prediction[0][0]
)

weights = model.layers[0].get_weights()

print(
    "\nWeights:"
)

print(
    weights
)