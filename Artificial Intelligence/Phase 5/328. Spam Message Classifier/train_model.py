import os
import pickle
import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dropout, Dense
from tensorflow.keras.callbacks import EarlyStopping


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "SMSSpamCollection"
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)

os.makedirs(
    OTHER_FILES,
    exist_ok=True
)

MODEL_PATH = os.path.join(
    OTHER_FILES,
    "spam_model.keras"
)

TOKENIZER_PATH = os.path.join(
    OTHER_FILES,
    "tokenizer.pkl"
)


VOCAB_SIZE = 5000
MAX_LENGTH = 100
EPOCHS = 20
BATCH_SIZE = 32


print("Loading dataset...")

data = pd.read_csv(
    DATASET_PATH,
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="latin-1"
)

print(f"Total messages: {len(data)}")


data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})


X = data["message"]
y = data["label"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


tokenizer = Tokenizer(
    num_words=VOCAB_SIZE,
    oov_token="<OOV>"
)

tokenizer.fit_on_texts(
    X_train
)


X_train = tokenizer.texts_to_sequences(
    X_train
)

X_test = tokenizer.texts_to_sequences(
    X_test
)


X_train = pad_sequences(
    X_train,
    maxlen=MAX_LENGTH,
    padding="post",
    truncating="post"
)

X_test = pad_sequences(
    X_test,
    maxlen=MAX_LENGTH,
    padding="post",
    truncating="post"
)


model = Sequential([

    tf.keras.Input(
        shape=(MAX_LENGTH,)
    ),

    Embedding(
        input_dim=VOCAB_SIZE,
        output_dim=64
    ),

    LSTM(
        64
    ),

    Dropout(
        0.5
    ),

    Dense(
        1,
        activation="sigmoid"
    )
])


model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


model.summary()


early_stopping = EarlyStopping(
    monitor="val_accuracy",
    patience=4,
    mode="max",
    restore_best_weights=True
)


print("\nStarting training...\n")


model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    callbacks=[early_stopping],
    verbose=1
)


print("\nEvaluating model...")


loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)


print(
    f"Test Accuracy: {accuracy * 100:.2f}%"
)


model.save(
    MODEL_PATH
)


with open(
    TOKENIZER_PATH,
    "wb"
) as file:

    pickle.dump(
        tokenizer,
        file
    )


print("\nModel saved successfully.")
print("Tokenizer saved successfully.")
print("\nTraining completed.")