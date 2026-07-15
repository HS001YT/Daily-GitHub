from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import sqlite3
import os

import pandas as pd

import matplotlib.pyplot as plt


app = Flask(__name__)


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "database.db"
)

CHART_PATH = os.path.join(
    BASE_DIR,
    "static",
    "expense_chart.png"
)


def create_database():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount REAL,
            category TEXT
        )
        """
    )

    connection.commit()

    connection.close()


create_database()


def classify_expense(
    description
):

    description = description.lower()

    if any(
        word in description
        for word in
        [
            "food",
            "pizza",
            "burger",
            "restaurant",
            "cafe"
        ]
    ):

        return "Food"

    if any(
        word in description
        for word in
        [
            "uber",
            "bus",
            "train",
            "fuel",
            "travel"
        ]
    ):

        return "Travel"

    if any(
        word in description
        for word in
        [
            "amazon",
            "shopping",
            "clothes"
        ]
    ):

        return "Shopping"

    if any(
        word in description
        for word in
        [
            "electricity",
            "water",
            "bill"
        ]
    ):

        return "Bills"

    if any(
        word in description
        for word in
        [
            "course",
            "book",
            "education"
        ]
    ):

        return "Education"

    return "Other"


@app.route("/")
def home():

    return render_template(
        "home.html"
    )


@app.route(
    "/add",
    methods=["GET", "POST"]
)
def add_expense():

    if request.method == "POST":

        description = request.form.get(
            "description"
        )

        amount = float(
            request.form.get(
                "amount"
            )
        )

        category = request.form.get(
            "category"
        )

        connection = sqlite3.connect(
            DATABASE_PATH
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO expenses
            (
                description,
                amount,
                category
            )
            VALUES
            (
                ?,
                ?,
                ?
            )
            """,
            (
                description,
                amount,
                category
            )
        )

        connection.commit()

        connection.close()

        return redirect(
            "/history"
        )

    return render_template(
        "add_expense.html"
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
        FROM expenses
        ORDER BY id DESC
        """
    )

    expenses = cursor.fetchall()

    connection.close()

    return render_template(
        "history.html",
        expenses=expenses
    )


@app.route("/dashboard")
def dashboard():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    df = pd.read_sql_query(
        "SELECT * FROM expenses",
        connection
    )

    connection.close()

    total_amount = 0
    total_transactions = 0
    top_expense = "N/A"

    if len(df) > 0:

        expense_totals = (
            df.groupby(
                "description"
            )["amount"]
            .sum()
        )

        total_amount = round(
            df["amount"].sum(),
            2
        )

        total_transactions = len(df)

        top_expense = (
            expense_totals.idxmax()
        )

        plt.figure(
            figsize=(10, 8)
        )

        wedges, texts, autotexts = plt.pie(
            expense_totals.values,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.legend(
            wedges,
            expense_totals.index,
            title="Expenses",
            loc="center left",
            bbox_to_anchor=(1, 0.5)
        )

        plt.title(
            "Expense Distribution"
        )

        plt.tight_layout()

        plt.savefig(
            CHART_PATH,
            bbox_inches="tight"
        )

        plt.close()

    return render_template(
        "dashboard.html",
        total_amount=total_amount,
        total_transactions=total_transactions,
        top_expense=top_expense
    )

if __name__ == "__main__":

    app.run(
        debug=True
    )