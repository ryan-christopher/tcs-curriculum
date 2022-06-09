#    H a n g m a n
#        ----|
#        |   |
#        O   |
#      - | - |
#        -   |
#       / \  |
#            |
#       ------
#  by Ryan

# import functions
from termcolor import colored
from random import choice
from time import sleep
import os

# array of possible words
words = ["dog", "test", "hello", "pancake", "doorway", "unicorn", "lexicon", "library",
        "cryptocurrency", "apple", "sandwich", "baseball", "basketball", "boston", "nevada",
        "coding", "painting", "orange"]

# array of possible hangman scenarios
hangman_positions = [ 
    """
        ----|
        |   |
            |
            |
            |
            |
            |
       ------
    """,

    """
        ----|
        |   |
        O   |
            |
            |
            |
            |
       ------
    """,

    """
        ----|
        |   |
        O   |
        |   |
        -   |
            |
            |
       ------
    """,

    """
        ----|
        |   |
        O   |
        |   |
        -   |
       /    |
            |
       ------
    """,

    """
        ----|
        |   |
        O   |
        |   |
        -   |
       / \  |
            |
       ------
    """,

    """
        ----|
        |   |
        O   |
      - |   |
        -   |
       / \  |
            |
       ------
    """,

    """
        ----|
        |   |
        O   |
      - | - |
        -   |
       / \  |
            |
       ------
    """
]

# get random word from list
secret_word = choice(words)
secret_word_spots = []

# create blank spot for player to guess
for i in range(len(secret_word)):
    secret_word_spots.append("_")

# empty array to store guessed letters
guessed_letters = []

# variable to track amount of tries
tries = 0

# checkresults function that takes an array for an argument
# and adds a correct letter to the puzzle
def checkresults(secret_word_spots):
    print("Correct!")
    sleep(1)
    correct = 0

    # iterate through the possible correct letters to decide
    # if the full word has gotten guessed
    for i in range(len(secret_word)):
        if secret_word[i] in guessed_letters:
            secret_word_spots[i] = secret_word[i]
            correct += 1
    
    # selection statement to check if the correct letters
    if correct == len(secret_word):
        print(colored("Y O U  W I N !", "green"))
        print("The secret word was: " + secret_word)
        return True
    
    # otherwise return False
    else:
        return False


        
    
# game loop, will run until a break statement occurs
while True:

    print(colored("   H A N G M A N ", "red"))
    print(hangman_positions[tries])
    current = ""

    for i in range(len(secret_word)):
        # create "fill in the blank" style word 
        # ex: test --> _ _ _ _
        current += secret_word_spots[i] + " "

    print(current)
    
    print("Guessed letters:  " + str(guessed_letters))

    # ask user for input
    guess = str(input(colored("What letter do you guess? ", "blue")))

    # prevent the player from guessing multiple letters at once
    while len(guess) != 1:
        guess = input(colored("Error, can only choose 1 letter.  Please pick again:  ", "blue")) 

    # prevent player from guessing the same letter multiple times
    while guess in guessed_letters:
        guess = input(colored("Letter already guessed.  Please pick again:  ", "blue"))

    # if the letter is not in the secret word, then add to the guessed letters array
    # and increase the number of tries to show the next version of the hangman pictures
    if guess not in secret_word:

        guessed_letters.append(guess)

        if tries < 5:
            tries += 1
            print("Nope!")
            sleep(1)
            os.system("clear")
        

        else:
            print(hangman_positions[6])
            print(colored("G A M E  O V E R", "red"))
            break
    
    # otherwise, call the checkresults to determine which letter was correctly guessed
    else:
        guessed_letters.append(guess)
        if checkresults(secret_word_spots):
            break
        os.system("clear")