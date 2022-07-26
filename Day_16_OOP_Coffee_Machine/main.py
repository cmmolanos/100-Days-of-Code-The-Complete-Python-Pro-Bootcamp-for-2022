from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine = CoffeeMaker()
payment_system = MoneyMachine()

while True:
    selection = input("What would you like? (espresso/latte/cappuccino/):").lower()

    if selection == 'off':
        break

    elif selection == 'report':
        machine.report()
        payment_system.report()

    else:
        coffee = Menu().find_drink(selection)

        if machine.is_resource_sufficient(coffee):
            if payment_system.make_payment(coffee.cost):
                machine.make_coffee(coffee)
