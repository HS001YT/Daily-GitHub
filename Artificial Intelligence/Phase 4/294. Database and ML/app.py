from flask import Flask
from flask import render_template
from flask import request

import sqlite3
import os


app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "database.db"
)


def create_database():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_text TEXT,
            prediction TEXT
        )
        """
    )

    connection.commit()

    connection.close()


create_database()


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    text = request.form.get(
        "text"
    )

    if not text:

        return render_template(
            "result.html",
            prediction="No Input"
        )

    if "good" in text.lower():

        prediction = "Positive"

    else:

        prediction = "Negative"

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO predictions
        (
            user_text,
            prediction
        )
        VALUES
        (
            ?,
            ?
        )
        """,
        (
            text,
            prediction
        )
    )

    connection.commit()

    connection.close()

    return render_template(
        "result.html",
        prediction=prediction
    )


@app.route("/history")
def history():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM predictions
        ORDER BY id DESC
        """
    )

    records = cursor.fetchall()

    connection.close()

    return render_template(
        "history.html",
        records=records
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )