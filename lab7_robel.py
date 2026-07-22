# TICKET 1 - Random Welcome Message

import random

welcome_messages = [
    "Welcome to our store! Happy shopping!",
    "Thanks for visiting our store today!",
    "Hello! We hope you find everything you need!"
]

print(random.choice(welcome_messages))


# TICKET 2 - Put an Item on Sale

# Add this method INSIDE your Item class

def set_price(self, amount):
    if amount < 0:
        print("Price cannot be negative!")
    else:
        self.price = amount

# After creating your items
# (Replace 'apple' with one of your item variable names.)

apple.set_price(0.75)
print("SALE! " + apple.name + " is now $" + str(apple.price) + "!")



# TICKET 3 - Show the Menu
 

print("\n===== MENU =====")

for number, item in store.items():
    print(number + ". " + item.name + " - $" + str(item.price))


# TICKET 4 


choice = input("Enter an item number or type 'done': ")

if choice == "done":
    shopping = False

elif choice in store:
    cart.add_item(store[choice])

else:
    print("Sorry, that's not on the menu!")


# TICKET 5

print("\n===== RECEIPT =====")

for item in cart.items:
    print(item.name + " - $" + str(item.price))


# TICKET 6 

print("\nYou bought " + str(len(cart.items)) + " item(s).")