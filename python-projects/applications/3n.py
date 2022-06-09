# 3n.py
# aka Collatz Conjecture
# start with any positive number
# if the number is even, the next term is half the previous term
# if the number is odd, the next term is three times the previous term, then add 1
from time import sleep
from termcolor import colored

while True:

    print("What number would you like to start with?")
    answer = input("--> ")

    while answer.isnumeric() != True or int(answer) < 1:

        print("Choose a number greater than zero.")
        answer = input("--> ")

    print("What length of time should each operation take?")
    interval = float(input("--> "))

    answer = int(answer)

    while answer > 1:

        if answer % 2 == 0:
            answer = answer // 2
            print(colored(answer, "red"))

        elif answer % 2 != 0:
            answer = (answer * 3) + 1
            print(colored(answer, "green"))

        sleep(interval)
