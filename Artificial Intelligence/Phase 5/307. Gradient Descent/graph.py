import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
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


x_train = np.array(
    [1, 2, 3, 4, 5, 6],
    dtype=np.float32
)

y_train = np.array(
    [10, 20, 30, 40, 50, 60],
    dtype=np.float32
)


learning_rates = [
    0.001,
    0.01,
    1.0
]


for lr in learning_rates:

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

    optimizer = tf.keras.optimizers.SGD(
        learning_rate=lr
    )

    model.compile(
        optimizer=optimizer,
        loss="mse"
    )

    history = model.fit(
        x_train,
        y_train,
        epochs=100,
        verbose=0
    )

    plt.figure(
        figsize=(8, 5)
    )

    plt.plot(
        history.history["loss"]
    )

    plt.title(
        f"Learning Rate = {lr}"
    )

    plt.xlabel(
        "Epoch"
    )

    plt.ylabel(
        "Loss"
    )

    plt.grid()

    file_name = (
        f"loss_lr_{str(lr).replace('.', '_')}.png"
    )

    save_path = os.path.join(
        OTHER_FILES_DIR,
        file_name
    )

    plt.savefig(
        save_path,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()

    print(
        f"\nLearning Rate: {lr}"
    )

    print(
        "Final Loss:",
        history.history["loss"][-1]
    )