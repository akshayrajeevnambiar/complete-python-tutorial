from art import print_calc_logo

def add(num1: float, num2: float) -> float:
    return num1 + num2

def sub(num1: float, num2: float) -> float:
    return num1 - num2

def mul(num1: float, num2: float) -> float:
    return num1 * num2

def div(num1: float, num2: float) -> float:
    return num1 / num2

def calc(num1: float, num2: float, operation: str) -> float:
    match operation:
        case '+' : 
            print(add(num1, num2))
        case '-' : 
            print(sub(num1, num2))
        case '*' : 
            print(mul(num1, num2))
        case '/' : 
            print(div(num1, num2))
        case _   : 
            print("Invalid operation")

def main():
    choice = ''
    while choice != 'n':
        print("\033c", end="")
        print_calc_logo()
        num1 = float(input("Enter the first number = "))
        num2 = float(input("Enter the second number = "))
        operator = input("What operation would you like to perform (+,-,*,/) = ")
        calc(num1, num2, operator)
        choice = input("Would you like to go again (y/n) = ")

main()


