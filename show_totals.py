# show_totals.py
# Person 2's part: Show total spent by category

def show_totals(filename="expenses.txt"):
    totals = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                amount = float(amount)
                totals[category] = totals.get(category, 0) + amount

        print("\n--- Total Spent by Category ---")
        for category, total in totals.items():
            print(f"{category}: ₹{total:.2f}")

    except FileNotFoundError:
        print("Error: Expense file not found. Please add expenses first.")

if __name__ == "__main__":
    show_totals()
