# Here we are going to create a coffee machine.

profit = 0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def espresso():
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
        print("Please insert coins.")
        tens = int(input("How many tens?: "))   
        fifties = int(input("How many fifties?: "))
        hundreds = int(input("How many hundreds?: "))

        total = (tens * 10) + (fifties * 50) + (hundreds * 100)
        if(total>= MENU["espresso"]["cost"]):
            change = total - MENU["espresso"]["cost"]
            print(f"Here is Rs{change} in change.")
            print(f"Here is your delicious espresso ☕️. Enjoy!")
            resources['water'] -= MENU["espresso"]["ingredients"]["water"]
            resources['coffee'] -= MENU["espresso"]["ingredients"]["coffee"]
            global profit
            profit += MENU["espresso"]["cost"]

        else:
            print("Sorry that's not enough money. Money refunded.")
    
    elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")

    elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")

    prompt()

def latte():
    if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
        print("Please insert coins.")
        tens = int(input("How many tens?: "))   
        fifties = int(input("How many fifties?: "))
        hundreds = int(input("How many hundreds?: "))

        total = (tens * 10) + (fifties * 50) + (hundreds * 100)
        if(total>= MENU["latte"]["cost"]):

            change = total - MENU["latte"]["cost"]
            print(f"Here is Rs{change} in change.")
            print(f"Here is your delicious latte ☕️. Enjoy!")
            resources['water'] -= MENU["latte"]["ingredients"]["water"]
            resources['milk'] -= MENU["latte"]["ingredients"]["milk"]
            resources['coffee'] -= MENU["latte"]["ingredients"]["coffee"]
            global profit
            profit += MENU["latte"]["cost"]

        else:
            print("Sorry that's not enough money. Money refunded.")

    elif resources["water"] < MENU["latte"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        
    elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        
    elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")


    prompt()

def cappuccino():
    if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] and resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
        print("Please insert coins.")
        tens = int(input("How many tens?: "))   
        fifties = int(input("How many fifties?: "))
        hundreds = int(input("How many hundreds?: "))

        total = (tens * 10) + (fifties * 50) + (hundreds * 100)
        if(total>= MENU["cappuccino"]["cost"]):
            change = total - MENU["cappuccino"]["cost"]
            print(f"Here is Rs{change} in change.")
            print(f"Here is your delicious capaccino ☕️. Enjoy!")
            resources['water'] -= MENU["cappuccino"]["ingredients"]["water"]
            resources['milk'] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources['coffee'] -= MENU["cappuccino"]["ingredients"]["coffee"]
            global profit
            profit += MENU["cappuccino"]["cost"]

        else:
            print("Sorry that's not enough money. Money refunded.")


    elif resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")

    elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")

    elif resources ['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")

    prompt()

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: Rs{profit}")

    prompt()
def off():
    exit()
def prompt():
    res = input("What would you like? (espresso/latte/cappuccino): ").lower()
   

    if res == "espresso":
        espresso()


    elif res == "latte":
        latte()

    elif res == "cappuccino":
        cappuccino()

    elif res == "report":
        report()
    
    elif res == "off":
        off()
    
    else:
        print("Invalid input. Please try again.")
        prompt()

prompt()
