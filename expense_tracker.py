import json

FILE_NAME = "expenses.json"
expenses = []


def load_expenses():
    global expenses

    try:
        with open(FILE_NAME, "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpenses")
    print("--------")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. "
            f"{expense['category']} - "
            f"Rs. {expense['amount']:.2f}"
        )


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal spending: Rs. {total:.2f}")


def main():
    load_expenses()

    while True:
        print("\nPersonal Expense Tracker")
        print("-----------------------")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


main()