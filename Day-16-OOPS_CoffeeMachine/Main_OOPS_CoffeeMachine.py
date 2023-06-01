###### MAIN FILE ######
'''
Functions
1) Print report
2) Check resources sufficient
3) Process coins
4) Check transaction successful
5) Make Coffee

'''

############ My Solution ############
'''
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# 1) Print report
coffee_maker = CoffeeMaker()
coffee_maker.report()

money_machine = MoneyMachine()
money_machine.report()


# 2) Check resources sufficient
menu = Menu()
items_names = menu.get_items()
choise = input(f"Choose from Items Available : {items_names} : ")
drink_ava = menu.find_drink(choise)

resource_Flag = True
if not coffee_maker.is_resource_sufficient(drink_ava):
    print("Resources Not Available!! ")
    resource_Flag = False


# 3) Process coins
money_given = float(input("Give money !! "))
'''


########## Angela's Solution ########## 

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
