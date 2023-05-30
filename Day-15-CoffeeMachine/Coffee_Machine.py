'''
Coffee Machine

Our Coffee Machine is going to make 3 hot coffee flavours. Espresso, Latte and Cappuccino.
Each flavour require different quantity of water, coffee and milk. And they are priced different as well.
The machine has 3 containers for Espresso, Latte and Cappuccino. The machine is coin operated, there are 4 types of coins.
The machine should print report depending upon the resources used.

'''
########################## My Solution ##########################
'''
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

exit_Flag = False
resource_Flag = False

def update(drink_name):
    global resources
    global resource_Flag
    global exit_Flag
    try:
        milk = MENU[drink_name]['ingredients']['milk']
    except KeyError:
        milk = 0
    water = MENU[drink_name]['ingredients']['water']
    coffee = MENU[drink_name]['ingredients']['coffee']
    
    if resources['water'] <= 0 or resources['milk'] <= 0 or resources['coffee'] <= 0:
        print("Not Enough Resources!!")
        exit_Flag = True
        resource_Flag = True
    else:    
        resources['water'] = resources['water'] - water
        resources['milk'] = resources['milk'] - milk
resources['coffee'] = resources['coffee'] - coffee
    
    

def calculate(q,d,n,p):
    price = (0.01*p) + (0.05*n) + (0.10*d) + (0.25*q)
    return(price)


def dispense():
    global exit_Flag
    question = input("What would you like to have (espresso/latte/cappuccino): ").lower()
    if question == 'report':
        print(resources)
    elif question == 'exit':
        print("Have a nice day!!")
        exit_Flag = True
    elif question == 'espresso' or question == 'latte' or question == 'cappuccino':
        print("Please insert coins!!")
        quarters_ask = int(input("How many quarters: "))
        dimes_ask = int(input("How many dimes: "))
        nickels_ask = int(input("How many nickels: "))
        pennies_ask = int(input("How many pennies: "))
        money_given = calculate(quarters_ask,dimes_ask,nickels_ask,pennies_ask)
        if money_given > MENU[question]["cost"]:
            print(f"Here is your {question}!!")
            balance_amt = money_given - MENU[question]["cost"]
            print(f"Your balence amount: {balance_amt }")
            update(question)
        elif money_given == MENU[question]["cost"]:
            print(f'Here is your {question}')
            update(question)
        else:
            print("Money not enough!!")
            print(f'You gave {money_given}, but the drink cost {MENU[question]["cost"]}')
    else:
        print("Uable to understand you. Please try again!!")

print("Welcome to Yashwanth's Coffee Machine!!")
while not exit_Flag:
    dispense()
    if resource_Flag:
        print("Please Call Yashwanth!!")
        break

'''
############################### Angela's Solution ###############################


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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])