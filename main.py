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


def print_resources():
    """"This method return the report for the coffee machine"""
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(resources["money"]))


def check_order_possibility(item):
    """"This method return True if we are able to but the specified item"""
    if item == "latte" or item == "cappuccino":
        if MENU[item]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
    if MENU[item]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    if MENU[item]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


def do_order(item):
    """""This method creates the order for the specified item"""
    global resources
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01

    amount = quarters + dimes + nickles + pennies
    if amount >= MENU[item]["cost"]:
        print("Here is $" + str(round(amount - MENU[item]["cost"], 2)) + " in change")
        print("Here is your " + item + "☕. Enjoy!")
        if item == "latte" or item == "cappuccino":
            resources["milk"] -= MENU[item]["ingredients"]["milk"]

        resources["water"] -= MENU[item]["ingredients"]["water"]
        resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
        resources["money"] += MENU[item]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")


# Add price in resources
resources["money"] = 0

stop = False
while not stop:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print_resources()
    elif order == "espresso" and check_order_possibility("espresso"):
        do_order("espresso")
    elif order == "latte" and check_order_possibility("latte"):
        do_order("latte")
    elif order == "cappuccino" and check_order_possibility("cappuccino"):
        do_order("cappuccino")
