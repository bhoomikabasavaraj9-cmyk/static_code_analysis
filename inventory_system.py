"""
Inventory Management System
This program allows adding, removing, saving, and loading inventory items.
Improved version with Pylint, Bandit, and Flake8 compliance.
"""

import json
from datetime import datetime

# Global variable to store stock data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add item quantity to stock data."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove item quantity from stock data safely."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: '{item}' not found in stock data.")
    except TypeError:
        print("Error: Invalid quantity type. Please enter a number.")


def get_qty(item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    with open(file_name, "r", encoding="utf-8") as file:
        stock_data = json.load(file)


def save_data(file_name="inventory.json"):
    """Save inventory data to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(stock_data, file)


def print_data():
    """Print all inventory items."""
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items with quantity below a threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("Safe code executed successfully.")


if __name__ == "__main__":
    main()
