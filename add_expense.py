# add_expense.py

def add_expense():
    category = input("Enter category (e.g. Food, Transport): ")
    amount = input("Enter amount: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{category},{amount}\n")

    print("Expense added successfully!")

if __name__ == "__main__":
    add_expense()
