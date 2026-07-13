from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

import sqlite3
import os


app = Flask(__name__)

app.secret_key = "my_secret_key"


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
        CREATE TABLE IF NOT EXISTS users
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
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
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        username = request.form.get(
            "username"
        )

        password = request.form.get(
            "password"
        )

        try:

            connection = sqlite3.connect(
                DATABASE_PATH
            )

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO users
                (
                    username,
                    password
                )
                VALUES
                (
                    ?,
                    ?
                )
                """,
                (
                    username,
                    password
                )
            )

            connection.commit()

            connection.close()

            return redirect(
                "/login"
            )

        except:

            return "Username already exists"

    return render_template(
        "register.html"
    )


@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form.get(
            "username"
        )

        password = request.form.get(
            "password"
        )

        connection = sqlite3.connect(
            DATABASE_PATH
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username=?
            AND password=?
            """,
            (
                username,
                password
            )
        )

        user = cursor.fetchone()

        connection.close()

        if user:

            session["user"] = username

            return redirect(
                "/dashboard"
            )

        return "Invalid Credentials"

    return render_template(
        "login.html"
    )


@app.route("/dashboard")
def dashboard():

    if "user" not in session:

        return redirect(
            "/login"
        )

    return render_template(
        "dashboard.html",
        username=session["user"]
    )


@app.route("/logout")
def logout():

    session.pop(
        "user",
        None
    )

    return redirect(
        "/"
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )