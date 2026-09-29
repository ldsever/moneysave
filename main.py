from db import init_db
init_db()
import argparse
from expense_manager import ExpenseManager

parser = argparse.ArgumentParser()

parser.add_argument("command")

parser.add_argument("--id", type=int)
parser.add_argument("--description")
parser.add_argument("--amount", type=int)
parser.add_argument("--month", type=int)

args = parser.parse_args()

if args.command == "add":
    manager = ExpenseManager()
    manager.add_expense(args.description, args.amount)

elif args.command == "list":
    manager = ExpenseManager()
    manager.list_expenses()

elif args.command == "summary":
    manager = ExpenseManager()
    if args.month is not None:
        manager.monthly_summary(args.month)
    else:
        manager.summary()

elif args.command == "delete":
    manager = ExpenseManager()
    manager.delete_expense(args.id)

elif args.command == "update":
    manager = ExpenseManager()
    manager.update_expense(args.id, args.description, args.amount)

elif args.command == "export":
    manager = ExpenseManager()
    manager.export_to_csv()

