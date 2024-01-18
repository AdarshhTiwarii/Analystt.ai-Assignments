import sqlite3
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                amount REAL,
                category TEXT,
                description TEXT,
                date TEXT
            )
        ''')
        self.conn.commit()

    def add_expense(self, amount, category, description=""):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
            INSERT INTO expenses (amount, category, description, date)
            VALUES (?, ?, ?, ?)
        ''', (amount, category, description, date))
        self.conn.commit()
        print("Expense added successfully!")

    def view_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        expenses = self.cursor.fetchall()
        if not expenses:
            print("No expenses available.")
        else:
            for expense in expenses:
                print(f"ID: {expense[0]}, Amount: Rs {expense[1]}, Category: {expense[2]}, Description: {expense[3]}, Date: {expense[4]}")

    def delete_expense(self, expense_id):
        self.cursor.execute("SELECT * FROM expenses WHERE id=?", (expense_id,))
        expense = self.cursor.fetchone()
        if expense:
            self.cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
            self.conn.commit()
            print(f"Expense with ID {expense_id} deleted successfully.")
        else:
            print("Expense not found.")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter expense description (optional): ")
            expense_tracker.add_expense(amount, category, description)
        elif choice == "2":
            expense_tracker.view_expenses()
        elif choice == "3":
            expense_id = int(input("Enter expense ID to delete: "))
            expense_tracker.delete_expense(expense_id)
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
