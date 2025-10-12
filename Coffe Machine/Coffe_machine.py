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
    "money": 0
}
running = True
def calculator(type):
    #TODO: money calculator
    print("Please insert coin.")
    quaters = float(input("How many quaters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    sum = ((quaters*(0.25))+dimes*(0.10)+nickles*(0.05)+pennies*(0.01))
    if sum >= MENU[type]["cost"] and resources["water"]>=MENU[type]["ingredients"]["water"] and resources["milk"] >= MENU[type]["ingredients"]["milk"] and resources["coffee"]>= MENU[type]["ingredients"]["coffee"]:
        #TODO:resource calculator
        resources["water"]-=MENU[type]["ingredients"]["water"]
        resources["milk"]-= MENU[type]["ingredients"]["milk"]
        resources["coffee"]-= MENU[type]["ingredients"]["coffee"]
        resources["money"]+=MENU[type]["cost"]
        if sum > MENU[type]["cost"]:
            change = round((sum-MENU[type]["cost"]),2)
            print(f'Here is your change: ${change}')
        print(f"Here is your {type}. Enjoy!\n")
    elif sum < MENU[type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry, there are not enough resources.")

while running:
    start = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if start =='report':
        print(f'Water:{resources["water"]}ml\nMilk:{resources["milk"]}ml\nCoffee:{resources["coffee"]}gm\nMoney:${resources["money"]}')
    elif start == 'latte':
        calculator('latte')
    elif start == 'espresso':
        calculator('espresso')
    elif start == 'cappuccino':
        calculator('cappuccino')
    elif start == 'off':
        running = False
    else:
        print("Wrong input try again")
