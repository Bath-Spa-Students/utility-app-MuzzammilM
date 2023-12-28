import random

class VendingMachine:
    def __init__(self):
        # Data Structures: Dictionaries for items and stock
        self.items = {
            'A1':{'name': 'Croissant', 'price': 2.00, 'category': 'Snacks'},
            'B2':{'name': 'Oman Chips', 'price': 1.00, 'category': 'Snacks'},
            'C3':{'name': 'Peanuts', 'price': 2.50, 'category': 'Snacks'},
            'D4':{'name': 'Lays chips', 'price': 1.75, 'category': 'Snacks'},

            'E5':{'name': 'Galaxy', 'price': 2.00, 'category': 'Chocolates'},
            'F6':{'name': 'Snickers', 'price': 1.25, 'category': 'Chocolates'},
            'G7':{'name': 'maltesars', 'price': 3.00, 'category': 'Chocolates'},
            'H8':{'name': 'Twix', 'price': 2.25, 'category': 'Chocolates'},

            'I9':{'name': 'Redbull', 'price': 3.25, 'category': 'Drinks'},
            'J1':{'name': 'coca cola', 'price': 1.50, 'category': 'Drinks'},
            'K2':{'name': 'Water', 'price': 1.00, 'category': 'Drinks'},
            'L3':{'name': 'Mountain Dew', 'price': 2.50, 'category': 'Drinks'},

            'M4':{'name': 'Karak Chai', 'price': 1.00, 'category': 'Hot beverages'},
            'N5':{'name': 'Coffee', 'price': 3.00, 'category': 'Hot beverages'},
            'O6':{'name': 'Latte', 'price': 4.50, 'category': 'Hot beverages'},
            'P7':{'name': 'Hot Chocolate', 'price': 3.75, 'category': 'Hot beverages'},
        }
# Add more items as needed
        self.stock = {item: 10 for item in self.items}

        # Control Flow: Initialization of user_balance and user_last_purchase
        self.user_balance = 0.0
        self.user_account_balance = 50.0  # Example initial account balance
        self.user_last_purchase = None
        self.bill_items = []

    # Function: Display the vending machine menu
    def display_menu(self):
        print("=== Vending Machine Menu ===")

        for code, item in self.items.items():
            print(f"{code}: {item['name']} - ${item['price']} ({item['category']})")

    # Function: Take user input for inserting money
    def input_money(self):
        try:
            self.user_balance += float(input("Insert money: $"))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            self.input_money()

    # Function: Take user input for selecting an item by name and validate the input
    def select_item(self):
        item_name = input("Enter the item name: ")
        item_name = item_name.capitalize()  # Convert to title case for case-insensitive comparison

        for item, details in self.items.items():
            if item_name == item:
                return item
        else:
            print("Item not found. Please try again.")
            return self.select_item()

    # Function: Dispense the selected item, update stock and user balance
    def dispense_item(self, item):
        if self.stock[item] > 0 and self.user_balance >= self.items[item]['price']:
            self.stock[item] -= 1
            self.user_balance -= self.items[item]['price']
            print(f"Dispensing {item} - {self.items[item]['name']}")
            print(f"Remaining stock: {self.stock[item]}")
            print(f"Your current balance: ${self.user_balance:.2f}")
            self.user_last_purchase = item
            self.bill_items.append(item)
        elif self.stock[item] == 0:
            print(f"Sorry, {item} is out of stock.")
        else:
            print("Insufficient funds. Please insert more money.")

    # Function: Ask the user if they want to buy another item
    def buy_additional_item(self):
        choice = input("Do you want to buy another item? (yes/no): ").lower()
        return choice == 'yes'

    # Function: Provide a suggestion based on the user's last purchase
    def suggest_purchase(self):
        if self.user_last_purchase:
            category = self.items[self.user_last_purchase]['category']
            suggestions = [item for item, details in self.items.items() if details['category'] == category and self.stock[item] > 0]
           

    # Function: Print a summary receipt at the end of the vending process
    def print_receipt(self):
        print("\n=== Receipt ===")
        print("Items Purchased:")
        for item in self.bill_items:
            print(f"{item} - {self.items[item]['name']}: ${self.items[item]['price']:.2f}")
        total_amount = sum(self.items[item]['price'] for item in self.bill_items)
        print(f"Total Amount Spent: ${total_amount:.2f}")
        print(f"Your remaining account balance: ${self.user_account_balance + self.user_balance:.2f}")
        print(f"Amount returned: ${self.user_balance:.2f}")
        print(f"Thank you for using the vending machine!")

    # Function: Main vending process with loops and control flow
    def vending_process(self):
        print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""")
        purchased_items = False

        while True:
            self.display_menu()
            self.input_money()
            item_name = self.select_item()
            self.dispense_item(item_name)
            self.suggest_purchase()

            if not self.buy_additional_item():
                break
            purchased_items = True

        if purchased_items:
            self.print_receipt()
        else:
            print("No items were purchased. Your initial amount is available for retrieval.")

# Main Program
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.vending_process()