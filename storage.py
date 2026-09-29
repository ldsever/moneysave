import json
from expense import Expense

def save_expenses(expenses):
    expenses_dict = []
    for expense in expenses:

        expenses_dict.append(expense.to_dict())

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(expenses_dict, file, ensure_ascii=False, indent=4)

def load_expenses():

    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        expenses = []

        for item in data:
            expense = Expense(
                item["id"],
                item["description"],
                item["amount"],
                item["date"]
            )
            expenses.append(expense)

        return expenses