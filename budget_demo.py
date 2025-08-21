from budget import Category, plot_spending, plot_balance_over_time
import time

if __name__ == "__main__":
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")

    # Simulated transactions with slight delays for timestamps
    food.deposit(500, "Paycheck")
    time.sleep(0.5)
    food.withdraw(120, "Groceries")
    time.sleep(0.5)
    food.withdraw(40, "Takeout")

    clothing.deposit(200, "Paycheck")
    time.sleep(0.5)
    clothing.withdraw(75, "Shoes")

    auto.deposit(300, "Paycheck")
    time.sleep(0.5)
    auto.withdraw(100, "Gas")
    time.sleep(0.5)
    auto.withdraw(60, "Repairs")

    # Print ledgers
    print(food, "\n")
    print(clothing, "\n")
    print(auto, "\n")

    # Charts
    plot_spending([food, clothing, auto], filename="spending_report.png")
    plot_balance_over_time([food, clothing, auto], filename="balance_report.png")

    print("Charts saved as 'spending_report.png' and 'balance_report.png'")