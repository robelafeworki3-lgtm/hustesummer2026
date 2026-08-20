# Hustle Final Project
# Sneaker and Clothing Tracker


# 1. THE BLUEPRINT
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # This makes sure the price is not negative
    def check_price(self):
        if self.price < 0:
            self.price = 0

    def show_item(self):
        print(self.name, "- $", self.price)


# 2. KIND 1 - SNEAKER
class Sneaker(Item):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def show_item(self):
        print("Sneaker:", self.name,
              "| Size:", self.size,
              "| Price: $", self.price)


# 3. KIND 2 - CLOTHING
class Clothing(Item):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def show_item(self):
        print("Clothing:", self.name,
              "| Brand:", self.brand,
              "| Price: $", self.price)


# 4. THE BOSS
class Store:
    def __init__(self):
        self.items = []

    # Add an item to the list
    def add_item(self, item):
        self.items.append(item)

    # Show every item
    def show_items(self):
        print("\n----- YOUR ITEMS -----")

        if len(self.items) == 0:
            print("Your list is empty.")
            return

        number = 1

        for item in self.items:
            print(number, end=". ")
            item.show_item()
            number += 1

    # Add all the prices
    def total_price(self):
        total = 0

        for item in self.items:
            total += item.price

        return total


# ----------------------------------
# MAIN PROGRAM
# ----------------------------------

store = Store()


# Start with 5 items
store.add_item(Sneaker("New Balance 550", 120, 10))
store.add_item(Sneaker("Nike Dunk Low", 130, 9))
store.add_item(Clothing("Spider Hoodie", 150, "Sp5der"))
store.add_item(Clothing("North Face Jacket", 200, "North Face"))
store.add_item(Sneaker("Air Jordan 1", 180, 10.5))


# Menu repeats until the user quits
while True:

    print("\n========================")
    print("      MY ITEM TRACKER")
    print("========================")
    print("1. Show my items")
    print("2. Add a sneaker")
    print("3. Add clothing")
    print("4. Show total value")
    print("5. Quit")

    choice = input("Choose an option: ")

    # Option 1
    if choice == "1":
        store.show_items()

    # Option 2
    elif choice == "2":
        name = input("Enter sneaker name: ")

        try:
            price = float(input("Enter price: "))
            size = float(input("Enter shoe size: "))

            if price < 0:
                print("Price cannot be negative.")
            else:
                sneaker = Sneaker(name, price, size)
                store.add_item(sneaker)
                print("Sneaker added!")

        except ValueError:
            print("Please enter a valid number.")

    # Option 3
    elif choice == "3":
        name = input("Enter clothing name: ")
        brand = input("Enter brand: ")

        try:
            price = float(input("Enter price: "))

            if price < 0:
                print("Price cannot be negative.")
            else:
                clothing = Clothing(name, price, brand)
                store.add_item(clothing)
                print("Clothing added!")

        except ValueError:
            print("Please enter a valid number.")

    # Option 4
    elif choice == "4":
        total = store.total_price()
        print("\nTotal value: $", round(total, 2))

    # Option 5
    elif choice == "5":
        print("Thanks for using the Item Tracker!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please choose 1-5.")