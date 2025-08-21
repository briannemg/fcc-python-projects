"""
Budget App (Portfolio Edition)
==============================

A clean, extensible budget management tool with categories,
transaction history, and spending charts.
"""

from __future__ import annotations
from typing import List
from datetime import datetime
import matplotlib.pyplot as plt
import csv
import json

class Transaction:
    """Represents a single transaction in a budget category."""

    def __init__(self, amount: float, description: str = ""):
        self.amount = float(amount)
        self.description = description
        self.timestamp = datetime.now()

    def __repr__(self) -> str:
        sign = "+" if self.amount >= 0 else "-"
        return f"{self.timestamp:%Y-%m-%d %H:%M} | {sign}{abs(self.amount):.2f} | {self.description}"
    
class Category:
    """Represents a budget category such as Food, Clothing or Entertainment."""

    def __init__(self, name: str):
        self.name = name
        self.ledger: List[Transaction] = []

    def __str__(self) -> str:
        header = f"{self.name} Ledger".center(40, "=")
        body = "\n".join(str(txn) for txn in self.ledger)
        footer = f"\n{'-'*40}\nBalance: {self.get_balance():.2f}"
        return f"{header}\n{body}{footer}"
    
    # -------------------------
    # Public API
    # -------------------------

    def deposit(self, amount: float, description: str = "") -> None:
        """Record a deposit in this category."""
        self.ledger.append(Transaction(amount, description))

    def withdraw(self, amount: float, description: str = "") -> bool:
        """Attempt to withdraw funds from this category."""
        if self.check_funds(amount):
            self.ledger.append(Transaction(-amount, description))
            return True
        return False
    
    def transfer(self, amount: float, other: Category) -> bool:
        """Transfer funds from this category to another."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def get_balance(self) -> float:
        """Return the current balance of this category."""
        return sum(txn.amount for txn in self.ledger)
    
    def check_funds(self, amount: float) -> bool:
        """Check if enough balance exists to cover `amount`."""
        return self.get_balance() >= amount
    
    # -------------------------
    # Data export
    # -------------------------

    def export_csv(self, filename: str) -> None:
        """Export this category's transactions to CSV."""
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Amount", "Description"])
            for txn in self.ledger:
                writer.writerow([txn.timestamp, txn.amount, txn.description])

    def export_json(self, filename: str) -> None:
        """Export this category's transactions to JSON."""
        data = [
            {
                "date": txn.timestamp.isoformat(),
                "amount": txn.amount,
                "description": txn.description,
            }
            for txn in self.ledger
        ]
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

# -------------------------
# Visualization
# -------------------------

def plot_spending(categories: List[Category], filename: str = "spending.png") -> None:
    """
    Generate a bar chart and pie chart showing spending per category.

    Args:
        categories: List of Category objects
        filename: Filename to save combined chart image
    """
    labels = [c.name for c in categories]
    spent = [
        sum(-txn.amount for txn in c.ledger if txn.amount < 0)
        for c in categories
    ]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Bar chart
    ax1.bar(labels, spent, color="skyblue", edgecolor="black")
    ax1.set_title("Spending by Category")
    ax1.set_ylabel("Amount Spent ($)")
    ax1.set_xlabel("Category")

    # Pie chart
    ax2.pie(spent, labels=labels, autopct="%1.1f%%", startangle=140)
    ax2.set_title("Spending Breakdown")

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_balance_over_time(categories: List[Category], filename: str = "balances.png") -> None:
    """
    Generate a line chart showing balance over time for each category.

    Args:
        categories: List of Category objects
        filename: Filename to save chart
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    for category in categories:
        txns = sorted(category.ledger, key=lambda t: t.timestamp)

        balances = []
        running_total = 0
        dates = []
        for txn in txns:
            running_total += txn.amount
            balances.append(running_total)
            dates.append(txn.timestamp)

        ax.plot(dates, balances, marker="o", label=category.name)

    ax.set_title("Balance Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Balance ($)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)

    fig.autofmt_xdate()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    