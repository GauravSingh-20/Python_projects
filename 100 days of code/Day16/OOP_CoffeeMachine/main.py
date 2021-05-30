from menu import Menu, MenuItem
from Coffee_Maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
isON=True

coffee_maker.report()
money_machine.report()

while isON:
    options=menu.get_items()
    choice=input(f"What would you like ? ({options})")
    if choice=="off":
        isON=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
