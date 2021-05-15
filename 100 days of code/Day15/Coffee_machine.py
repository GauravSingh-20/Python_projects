from Menu import MENU,resources

logo= ''' 
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~



        COFFEE MACHINE
'''

print(logo+"\n\n")

def isResourceSufficient(order_ingredient):
    """Checks if the ingredients are sufficient"""

    for item in order_ingredient:
        if order_ingredient[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():

    """ Returns the total of the coins processed """

    print("Please insert coins ")
    total=int(input("How many quaters : "))*0.25
    total+=int(input("How many dimes : "))*0.10
    total+=int(input("How many nickels : "))*0.05
    total+=int(input("How many pennies : "))*0.01
    return total


def isTransactionSuccessful(money_recieved, drink_cost):
    """Returns true when payment is accepted or False if money is insufficient"""

    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"Here is ${change} in change ")
        global profit
        profit+= drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money Refunded")
        return False    


def makeCoffee(drink_name,order_ingredients):
    for item in resources:
        resources[item]-=order_ingredients[item]

    print(f"ere is your {drink_name}  ☕")

profit=0

isOn=True

while isOn:
    user_choice=input("“What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice=="off":
        isOn=False
    elif user_choice=="report":
        print(f"water : {resources['water']} ml" )
        print(f"milk : {resources['milk']} ml" )        
        print(f"coffee : {resources['coffee']} gm" )
        print(f"Money : {profit}")

    else:
        drink=MENU[user_choice]
        if isResourceSufficient(drink['ingredients']):
            payment=process_coins()
            if isTransactionSuccessful(payment,drink["cost"]):
                makeCoffee(user_choice,drink['ingredients'])