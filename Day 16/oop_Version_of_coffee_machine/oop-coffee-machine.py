from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_mc = MoneyMachine()
cofee_maker = CoffeeMaker()
menu = Menu()
is_on = True



while is_on :
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        cofee_maker.report()
        money_mc.report()
    else :
        drink = menu.find_drink(choice)
        if cofee_maker.is_resource_sufficient(drink):
            if money_mc.make_payment(drink.cost) :
                cofee_maker.make_coffee(drink)