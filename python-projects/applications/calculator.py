# calculator 
# by Ryan

from time import sleep
from termcolor import colored

def add(x, y):
    return(x + y)

def subtract(x, y):
    return(x - y)

def multiply(x, y):
    return(x * y)

def divide(x, y):
    return(x / y)

print("Hello, welcome to the Python Calculator Program.")
sleep(0.5)


while True:

    print("Please select a function:  ")
    print("to end application, enter quit.")
    response = input(colored("add, subtract, multiply, or divide ", "green"))


    while response not in ["add", "subtract", "multiply", "divide", "quit"]:
        print("Error, response is not one of the supported answers.")
        print("to end application, enter quit.")
        response = input(colored("add, subtract, multiply, or divide ", "green"))
    
    if response == "quit":
        print("Closing application now.")
        sleep(1)
        print("Thank you for using Python Calculator Program.")
        sleep(1)
        break

    num1 = int(input(colored("first number: ", "blue")))
    num2 = int(input(colored("second number: ", "blue")))

    if response == "add":
        answer = add(num1, num2)
        print("The addition of " + str(num1) + " and " + str(num2)+ " is " + colored(str(answer), "yellow") + ".")

    elif response == "subtract":
        answer = subtract(num1, num2)
        print("The subtraction of " + str(num1) + " and " + str(num2)+ " is " + colored(str(answer), "yellow") + ".")

    elif response == "multiply":
        answer = multiply(num1, num2)
        print("The multiplication of " + str(num1) + " and " + str(num2)+ " is " + colored(str(answer), "yellow") + ".")

    elif response == "divide":
        answer = divide(num1, num2)
        print("The division of " + str(num1) + " and " + str(num2)+ " is " + colored(str(answer), "yellow") + ".")


