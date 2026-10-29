"""Coffee Machine: A coin-operated beverage dispenser simulator."""


MENU = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.50},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.50},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.00},
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

def check_drink(drink):
    return drink in MENU

def check_resources(drink):
    """Return True if machine has enough resources for drink."""
    for item in ["water", "milk", "coffee"]:
        if resources[item] < MENU[drink][item]:
            return False
    return True

def collect_coins():
    print("Insert coins.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    return quarters, dimes, nickels

def process_coins():
    """Collect coin counts and return total monetary value."""
    quarters, dimes, nickels = collect_coins()
    return quarters*0.25 + dimes*0.1 + nickels*0.05

def process_payment(drink, payment):
    return payment >= MENU[drink]["cost"]

def dispense_drink(drink, payment):
    """Handle payment, change, and ingredient deduction. Return True if successful."""
    if not process_payment(drink, payment):
        print("Not enough money. Money refunded.")
        return False
    change = payment - MENU[drink]["cost"]
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
    for item in ["water", "milk", "coffee"]:
        resources[item] -= MENU[drink][item]
    resources["money"] += MENU[drink]["cost"]
    print(f"Here is your {drink}. Enjoy!")
    return True


def print_report():
    """Display current water, milk, coffee, and money in machine."""
    print(resources)


def main():
    """Main game loop: prompt for drink, handle commands, serve drinks."""
    choice = input("What do you want? (espresso/latte/cappuccino): ")
    if choice == "off":
        return
    elif not check_drink(choice):
        print("Invalid choice.")
        return
    elif choice == "report":
        print_report()
    else:
        if not check_resources(choice):
            print("Not enough resources.")
            return
        print("Preparing your drink...")
        payment = process_coins()
        dispense_drink(choice, payment)


if __name__ == "__main__":
    main()
