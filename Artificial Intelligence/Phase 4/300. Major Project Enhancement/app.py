from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import send_file

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

import os


app = Flask(__name__)


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE_FOLDER = os.path.join(
    BASE_DIR,
    "database"
)

DATABASE_PATH = os.path.join(
    DATABASE_FOLDER,
    "database.db"
)

STATIC_FOLDER = os.path.join(
    BASE_DIR,
    "static"
)

CHART_FOLDER = os.path.join(
    STATIC_FOLDER,
    "charts"
)

CHART_PATH = os.path.join(
    CHART_FOLDER,
    "expense_chart.png"
)

EXPORT_FOLDER = os.path.join(
    BASE_DIR,
    "exports"
)


os.makedirs(
    DATABASE_FOLDER,
    exist_ok=True
)

os.makedirs(
    CHART_FOLDER,
    exist_ok=True
)

os.makedirs(
    EXPORT_FOLDER,
    exist_ok=True
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
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            created_at TEXT NOT NULL
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
    methods=["GET", "POST"]
)
def add_expense():

    if request.method == "POST":

        description = request.form.get(
            "description"
        ).strip()

        amount = request.form.get(
            "amount"
        )

        if not description:

            return render_template(
                "add_expense.html",
                error="Description is required"
            )

        try:

            amount = float(
                amount
            )

        except:

            return render_template(
                "add_expense.html",
                error="Amount must be numeric"
            )

        if amount <= 0:

            return render_template(
                "add_expense.html",
                error="Amount must be greater than zero"
            )

        created_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
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
                created_at
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
                created_at
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

    search = request.args.get(
        "search",
        ""
    )

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    if search:

        cursor.execute(
            """
            SELECT *
            FROM expenses
            WHERE description
            LIKE ?
            ORDER BY id DESC
            """,
            (
                f"%{search}%",
            )
        )

    else:

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
        expenses=expenses,
        search=search
    )


@app.route(
    "/edit/<int:expense_id>",
    methods=["GET", "POST"]
)
def edit_expense(
    expense_id
):

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    if request.method == "POST":

        description = request.form.get(
            "description"
        ).strip()

        amount = request.form.get(
            "amount"
        )

        try:

            amount = float(
                amount
            )

        except:

            connection.close()

            return "Invalid Amount"

        cursor.execute(
            """
            UPDATE expenses
            SET
            description=?,
            amount=?
            WHERE id=?
            """,
            (
                description,
                amount,
                expense_id
            )
        )

        connection.commit()

        connection.close()

        return redirect(
            "/history"
        )

    cursor.execute(
        """
        SELECT *
        FROM expenses
        WHERE id=?
        """,
        (
            expense_id,
        )
    )

    expense = cursor.fetchone()

    connection.close()

    return render_template(
        "edit_expense.html",
        expense=expense
    )


@app.route(
    "/delete/<int:expense_id>"
)
def delete_expense(
    expense_id
):

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE
        FROM expenses
        WHERE id=?
        """,
        (
            expense_id,
        )
    )

    connection.commit()

    connection.close()

    return redirect(
        "/history"
    )


@app.route("/dashboard")
def dashboard():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    df = pd.read_sql_query(
        """
        SELECT *
        FROM expenses
        """,
        connection
    )

    connection.close()

    total_amount = 0
    total_transactions = 0
    average_expense = 0
    top_expense = "N/A"
    highest_transaction = 0
    lowest_transaction = 0

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

        total_transactions = len(
            df
        )

        average_expense = round(
            df["amount"].mean(),
            2
        )

        top_expense = (
            expense_totals.idxmax()
        )

        highest_transaction = round(
            df["amount"].max(),
            2
        )

        lowest_transaction = round(
            df["amount"].min(),
            2
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
            title="Expense Titles",
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
        average_expense=average_expense,
        top_expense=top_expense,
        highest_transaction=highest_transaction,
        lowest_transaction=lowest_transaction
    )


@app.route("/export")
def export_csv():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    df = pd.read_sql_query(
        """
        SELECT *
        FROM expenses
        """,
        connection
    )

    connection.close()

    export_path = os.path.join(
        EXPORT_FOLDER,
        "expenses.csv"
    )

    df.to_csv(
        export_path,
        index=False
    )

    return send_file(
        export_path,
        as_attachment=True
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )