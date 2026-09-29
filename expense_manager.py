import csv
from datetime import date
from db import (
    load_expenses,
    db_add_expense,
    delete_expense_by_id,
    update_expense_by_id,
)

class ExpenseManager:
    def __init__(self):
        self.expenses = load_expenses()


    def add_expense(self, description, amount):
        expense_date = str(date.today())
        new_id = db_add_expense(description, amount, expense_date)
        self.expenses = load_expenses()
        print(f"Expense added successfully (ID: {new_id})")

    def list_expenses(self):
        print(f"{'ID':<4}{'Date':<12}{'Description':<15}{'Amount':>6}")
        for expense in self.expenses:
            print(f"{expense.id:<4}{expense.date:<12}{expense.description:<15}{expense.amount:>6}")

    def summary(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        print(f"Total expenses: ${total}")

    def delete_expense(self, expense_id):
        rows = delete_expense_by_id(expense_id)
        self.expenses = load_expenses()

        if rows > 0:
            print("Expense deleted successfully")
        else:
            print("Expense not found")

    def update_expense(self, expense_id, description=None, amount=None):
        rows = update_expense_by_id(expense_id, description, amount)
        self.expenses = load_expenses()

        if rows > 0:
            print("Expense deleted successfully")
        else:
            print("Expense not found")
                         
    def monthly_summary(self, month):
        total = 0

        for expense in self.expenses:
            expense_month = int(expense.date.split("-")[1])

            if expense_month == month:
                total += expense.amount
        
        print(f"Total expenses for month {month}: ${total}")
            
    def export_to_csv(self):
        with open("expenses.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Date", "Description", "Amount"])

            for expense in self.expenses:
                writer.writerow([expense.id, expense.date, expense.description, expense.amount])

        print("Expenses exported successfully")


                            
                        
