from flask import Flask
from flask import render_template
from flask import request
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE_FOLDER = os.path.join(
    BASE_DIR,
    "database"
)

if not os.path.exists(
    DATABASE_FOLDER
):
    os.makedirs(
        DATABASE_FOLDER
    )

DATABASE_PATH = os.path.join(
    DATABASE_FOLDER,
    "students.db"
)


def create_database():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """
    )

    connection.commit()

    connection.close()


create_database()


@app.route("/")
def home():

    return render_template(
        "home.html"
    )


@app.route(
    "/add",
    methods=["POST"]
)
def add_student():

    name = request.form.get(
        "name"
    )

    age = request.form.get(
        "age"
    )

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (
            name,
            age
        )
        VALUES
        (
            ?,
            ?
        )
        """,
        (
            name,
            age
        )
    )

    connection.commit()

    connection.close()

    return (
        "Record Added Successfully"
    )


@app.route("/records")
def records():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        """
    )

    data = cursor.fetchall()

    connection.close()

    return render_template(
        "records.html",
        records=data
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )