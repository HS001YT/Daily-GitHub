from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

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

os.makedirs(
    DATABASE_FOLDER,
    exist_ok=True
)

DATABASE_PATH = os.path.join(
    DATABASE_FOLDER,
    "students.db"
)


def get_connection():

    return sqlite3.connect(
        DATABASE_PATH
    )


def create_table():

    connection = get_connection()

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


create_table()


@app.route("/")
def home():

    return render_template(
        "home.html"
    )


# -------------------------
# CREATE
# -------------------------

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

    connection = get_connection()

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

    return redirect(
        url_for(
            "records"
        )
    )


# -------------------------
# READ
# -------------------------

@app.route("/records")
def records():

    connection = get_connection()

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


# -------------------------
# UPDATE PAGE
# -------------------------

@app.route("/edit/<int:id>")
def edit(id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE id = ?
        """,
        (
            id,
        )
    )

    student = cursor.fetchone()

    connection.close()

    return render_template(
        "update.html",
        student=student
    )


# -------------------------
# UPDATE RECORD
# -------------------------

@app.route(
    "/update/<int:id>",
    methods=["POST"]
)
def update(id):

    name = request.form.get(
        "name"
    )

    age = request.form.get(
        "age"
    )

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE students
        SET
            name = ?,
            age = ?
        WHERE id = ?
        """,
        (
            name,
            age,
            id
        )
    )

    connection.commit()

    connection.close()

    return redirect(
        url_for(
            "records"
        )
    )


# -------------------------
# DELETE
# -------------------------

@app.route("/delete/<int:id>")
def delete(id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM students
        WHERE id = ?
        """,
        (
            id,
        )
    )

    connection.commit()

    connection.close()

    return redirect(
        url_for(
            "records"
        )
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )