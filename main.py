from data import MENU, resources


def cashier(drink):
    print("Please insert coins.")
    quarters = float(input("how many quarters? ")) * 0.25
    dimes = float(input("how many dimes? ")) * 0.10
    nickles = float(input("how many nickles? ")) * 0.05
    pennies = float(input("how many pennies? ")) * 0.01
    total_payment = quarters + dimes + nickles + pennies
    if total_payment >= chosen_coffee_price:
        change = round(total_payment - chosen_coffee_price, 3)
        print(f"Here is your ${change} in change.")
        print(f"Here is your {drink} ☕. Enjoy ^-^")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def machine_resources():
    sufficient_ingredients = True
    missing_item = ""
    if chosen_coffee_ingredients["water"] > machine_water:
        sufficient_ingredients = False
        missing_item = "water"
    elif chosen_coffee_ingredients["milk"] > machine_milk:
        sufficient_ingredients = False
        missing_item = "milk"
    elif chosen_coffee_ingredients["coffee"] > machine_coffee:
        sufficient_ingredients = False
        missing_item = "coffee"

    if sufficient_ingredients:
        return True
    else:
        print(f"Sorry there is not enough {missing_item}.")
        return False


money = 0
turn_on = True
machine_water = resources["water"]
machine_milk = resources["milk"]
machine_coffee = resources["coffee"]
while turn_on:
    coffee_type = input("  What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_type == "off":
        turn_on = False

    elif coffee_type == "report":
        print(f"Water: {machine_water}ml")
        print(f"Milk: {machine_milk}ml")
        print(f"Coffee: {machine_coffee}g")
        print(f"Money: ${money}")

    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        chosen_coffee = MENU[f"{coffee_type}"]
        chosen_coffee_price = chosen_coffee["cost"]
        chosen_coffee_ingredients = chosen_coffee["ingredients"]
        if machine_resources():
            if cashier(coffee_type):
                machine_water -= chosen_coffee_ingredients["water"]
                machine_milk -= chosen_coffee_ingredients["milk"]
                machine_coffee -= chosen_coffee_ingredients["coffee"]
                money += chosen_coffee_price

    else:
        print("Invalid info!")
