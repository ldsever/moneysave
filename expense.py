from datetime import date

class Expense:

    def __init__(self, id, description, amount, expense_date=None):
        self.id = id
        self.description = description
        self.amount = amount
        if expense_date:
            self.date = expense_date
        else:
            self.date = str(date.today())
        
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "date": self.date
        }

    def __str__(self):
        return f"ID: {self.id}, Description: {self.description}, Amount: {self.amount}, Date: {self.date}"