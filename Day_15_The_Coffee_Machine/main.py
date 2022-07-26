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

global resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    'quarters': 0.25,
    'dimes': 0.1,
    'nickles': 0.05,
    'pennies': 0.01
}

global money
money = 0


def print_report(res: dict, money: int):
    """Prints the report of the current state of resources and money"""
    print(f"Water: {res['water']}ml"
          f"Milk: {res['milk']}ml"
          f"Coffee: {res['coffee']}g"
          f"Money: ${money}")


def check_resources(sel: str, men: dict, res: dict) -> str:
    """
    Checks resources and print if one is run out
    Args:
        sel: selected type of coffee.
        men: menu directory
        res: resources directory to check availability.
    """
    for ing in res.keys():
        current_amount = men.get(sel).get("ingredients").get(ing, 0)
        if current_amount > res[ing]:
            return f"Sorry there is not enough {ing}."

    return "OK"


def sum_coins() -> int:
    """
    sum the coins
    Returns:
        int: total ammount of money.
    """
    print("Please insert coins:")
    total = 0

    for coin, value in coins.items():
        qty = int(input(f"How many {coin}?:"))
        total += qty * value

    return total


def make_cofee(selection: str, menu: dict):
    """

    Args:
        money:
        selection:
        menu:
        resources:

    Returns:

    """
    if total > menu[selection]["cost"]:
        change = round(total - menu[selection]['cost'], 2)
        print(f"Here is ${change} dollars in change.")

    money += menu[selection]['cost']

    for ing in resources.keys():
        resources[ing] -= menu.get(selection).get("ingredients").get(ing, 0)

    print(f"Here is your {selection} ☕ . Enjoy!")


if __name__ is '__main__':

    while True:
        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if selection == 'off':
            break

        elif selection == 'report':
            print_report(resources, money)

        elif selection in ('espresso', 'latte', 'cappuccino'):

            availability = check_resources(selection, MENU, resources)

            if availability is not 'OK':
                print(availability)

            else:

                total = sum_coins()

                if total < MENU[selection]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                    pass

                else:
                    make_cofee(selection, MENU)
