class Budget_Tracker:
    
    def __init__(self):
        self.budget = 0.0
        self.expenses = []

    def set_budget(self):
        try:
            self.budget = float(input("Enter your total budget: P" ))
            print(f"Your budget of P{self.budget:.2f} has been set.\n")

        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    def add_expense(self): 
        try:
            category = input("Enter the expense category (e.g, Food, Rent, etc.): ")
            amount = float(input(f"Enter expense amount for {category}: P"))
            self.expenses.append({"category": category, "amount": amount})
            print(f"Expense of P{amount:.2f} added under category '{category}'.\n")

        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.\n")
            return
        print("\nExpenses:")
        total_spent = 0.0

        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. {expense['category']}: P{expense['amount']:.2f}")
            total_spent += expense['amount']
        
        print(f"\nTotal spent: P{total_spent:.2f}")
        remaining_budget = self.budget - total_spent

        if self.budget > 0:
            print(f"Remaining budget: P{remaining_budget:.2f}\n")

    def show_menu(self):
        while True:
            print("""
== Budget Tracker Menu===

1. Set Budget
2. Add Expense
3. View Expenses
4. Exit
""")
            choice = input("Choose an option: ")
            if choice == "1":
                self.set_budget()
            elif choice == "2":
                self.add_expense()
            elif choice == "3":
                self.view_expenses()
            elif choice == "4":
                print("Exiting Budget Tracker.")
                break
            else:
                print("Invalid choice. Please select a valid option.\n")

# Run the Budget Tracker

if __name__== "__main__":
    app = Budget_Tracker()
    app.show_menu()
