import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf


values = tf.constant(
    [
        -3,
        -2,
        -1,
        0,
        1,
        2,
        3
    ],
    dtype=tf.float32
)

print(
    "\nOriginal Values:"
)

print(
    values.numpy()
)

print(
    "\nReLU Output:"
)

print(
    tf.nn.relu(
        values
    ).numpy()
)

print(
    "\nSigmoid Output:"
)

print(
    tf.nn.sigmoid(
        values
    ).numpy()
)

print(
    "\nTanh Output:"
)

print(
    tf.nn.tanh(
        values
    ).numpy()
)