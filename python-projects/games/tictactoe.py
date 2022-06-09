# Tic Tac Toe
#
#    x | o  | o
#  --------------
#    o | x  | x
#  --------------
#    o | x  | o
# 
# by Ryan

# import statements for helping with CPU opponent
# and animations


from random import randint
from time import sleep
import sys, os
from termcolor import colored

def animate(text, time):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(time)

animate("Tic Tac Toe\n", 0.1)

X = colored("X", "red")
O = colored("O", "cyan")

board = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

fullspots = 0

def generategrid(list):
  animate(list[1] + " | " + list[2] + " | " + list[3] + "\n", 0.025)
  animate("---------\n", 0.025)
  animate(list[4] + " | " + list[5] + " | " + list[6] + "\n", 0.025)
  animate("---------\n", 0.025)
  animate(list[7] + " | " + list[8] + " | " + list[9] + "\n\n\n", 0.025)


def checkspots(grid):
    if grid[1] == grid[4] == grid[7]:
        if grid[1] == X:
            animate(colored("You win!", "green"), 0.1)
        else:
            animate(colored("Computer wins!", "red"), 0.3)
        return True
    if grid[2] == grid[5] == grid[8]:
        if grid[2] == X:
            animate(colored("You win!", "green"), 0.1)
        else:
            animate(colored("Computer wins!", "red"), 0.3)
        return True
    if grid[3] == grid[6] == grid[9]:
        if grid[3] == X:
            animate(colored("You win!", "green"), 0.1)
        else:
            animate(colored("Computer wins!", "red"), 0.3)
        return True
    if grid[1] == grid[2] == grid[3]:
        if grid[1] == X:
            animate(colored("You win!", "green"), 0.1)
        else:
            animate(colored("Computer wins!", "red"), 0.3)
        return True
    if grid[4] == grid[5] == grid[6]:
        if grid[4] == X:
            animate(colored("You win!", "green"), 0.1)
        else:
            animate(colored("Computer wins!", "red"), 0.3)
        return True
    if grid[7] == grid[8] == grid[9]:
        if grid[7] == X:
            animate(colored("You win!", "green"), 0.1)
        else:
            animate(colored("Computer wins!", "red"), 0.3)
        return True
    if grid[1] == grid[5] == grid[9]:
        if grid[1] == X:
            animate(colored("You win!", "green"), 0.1)
        else:
            animate(colored("Computer wins!", "red"), 0.3)
        return True
    if grid[3] == grid[5] == grid[7]:
        if grid[3] == X:
            animate(colored("You win!", "green"), 0.1)
        else:
            animate(colored("Computer wins!", "red"), 0.3)
        return True

    return False


generategrid(board)

while True:
    animate("Which space do you choose?: ", 0.05)
    player = input("-> ")

    os.system("clear")

    while player.isnumeric() != True or int(player) > 9 or int(player) < 1 or board[int(player)] == X or board[int(player)] == O:
        if player.isnumeric() != True:
            player = input("Choose a number...")
        elif int(player) > 9 or int(player) < 1:
            player = input("That's not a valid number...")
        else:
            player = input("That's taken!")
        
    player = int(player)


    board[player] = X
    fullspots += 1
    generategrid(board)

    if checkspots(board) == True:
        break

    if fullspots == 9:
        print("Draw!!!")
        break

    cpu = randint(1, 9)

    while board[cpu] == X or board[cpu] == O:
        cpu = randint(1, 9)

    board[cpu] = O
    fullspots += 1
    sleep(1)
    generategrid(board)

