import sqlite3
from expense import Expense


def connect():
    return sqlite3.connect("expenses.db")

def init_db():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                amount INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        """)
def load_expenses():
    with connect() as conn:
        cursor = conn.execute("SELECT id, description, amount, date FROM expenses")
        rows = cursor.fetchall()

    expenses = []
    for row in rows:
        expense = Expense(row[0], row[1], row[2], row[3])
        expenses.append(expense)

    return expenses

def db_add_expense(description, amount, expense_date):
    with connect() as conn:
        cursor = conn.execute(
            "INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)",
            (description, amount, expense_date)
        )
        return cursor.lastrowid

def delete_expense_by_id(expense_id):
    with connect() as conn:
        return conn.execute(
            "DELETE FROM expenses WHERE id = ?",
            (expense_id,)
        ).rowcount

def update_expense_by_id(expense_id, description=None, amount=None):
    with connect() as conn:
        if description is not None and amount is not None:
            return conn.execute(
                "UPDATE expenses SET description = ?, amount = ? WHERE id = ?",
                (description, amount, expense_id)
            ).rowcount

        elif description is not None:
            return conn.execute(
                "UPDATE expenses SET description = ? WHERE id = ?",
                (description, expense_id)
            ).rowcount

        elif amount is not None:
            return conn.execute(
                "UPDATE expenses SET amount = ? WHERE id = ?",
                (amount, expense_id)
            ).rowcount

        return 0