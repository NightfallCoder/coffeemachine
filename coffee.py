MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# collect and process money
def process_money(user_choice, p, d, n, q):
    penny = 0.01
    dime = 0.10
    nickle = 0.05
    quarter = 0.25
    process_quarter = quarter * q
    process_dime = dime * d
    process_nickle = nickle * n
    process_penny = penny * p
    total_coins = process_quarter + process_penny + process_dime + process_nickle
    
    if user_choice in MENU:
        drink_cost = MENU[user_choice]["cost"]
        change = total_coins - drink_cost
        
        if change >= 0:
            print(f"Here is ${change} in change.")
            print(f"Here is your {user_choice} ☕.")
            deduct_resources(user_choice)
        else:
            print("Sorry, you don't have enough money for this drink.")

def deduct_resources(user_choice):
    for ingredient, amount in MENU[user_choice]["ingredients"].items():
        resources[ingredient] -= amount

# coffee logo
from art import coffee
print(coffee)

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()
    
    if user_choice == 'exit':
        print("Exiting the coffee machine. Have a great day!")
        break
    
    if user_choice == 'report':
        for resource, amount in resources.items():
            print(f"{resource.capitalize()}: {amount} units")
    else:
        print("Please insert coins: ")
        pennies = float(input("How much penny: $"))
        dimes = float(input("How much dime: $"))
        nickels = float(input("How much nickle: $"))
        quarters = float(input("How much quarter: $"))
        
        process_money(user_choice, pennies, dimes, nickels, quarters)
