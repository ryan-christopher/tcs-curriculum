from random import choice, randint
from time import sleep
import os

# Function to animate the text to look like an actual game
def animatetext(text):
    output = ""
    for i in range(len(text)):
        os.system("clear")
        output += text[i]
        print(output)
        sleep(0.005)

# helper function to print out the values of a list of card names
def printlist(list):
    output = ""
    for i in range(1, len(list)+1):
        output += """
        Card """ + str(i) + """: """ + list[i-1]
    return output

# helper function to add all the card values of a hand
def totalvalues(list):
    totalVal = 0
    for i in range(len(list)):
        totalVal += list[i]
    return totalVal


# create card suites and assign their values using
# dictionaries of key:value pairs
hearts =   {"2 of Hearts":2, "3 of Hearts":3, "4 of Hearts":4,
            "5 of Hearts":5, "6 of Hearts":6, "7 of Hearts":7, 
            "8 of Hearts":8, "9 of Hearts":9, "10 of Hearts":10,
            "Jack of Hearts": 10, "Queen of Hearts":10, 
            "King of Hearts":10, "Ace of Hearts":11}

diamonds = {"2 of Diamonds":2, "3 of Diamonds":3, "4 of Diamonds":4,
            "5 of Diamonds":5, "6 of Diamonds":6, "7 of Diamonds":7, 
            "8 of Diamonds":8, "9 of Diamonds":9, "10 of Diamonds":10,
            "Jack of Diamonds": 10, "Queen of Diamonds":10, 
            "King of Diamonds":10, "Ace of Diamonds":11}

clubs =    {"2 of Clubs":2, "3 of Clubs":3, "4 of Clubs":4,
           "5 of Clubs":5, "6 of Clubs":6, "7 of Clubs":7, 
           "8 of Clubs":8, "9 of Clubs":9, "10 of Clubs":10,
           "Jack of Clubs": 10, "Queen of Clubs":10, 
           "King of Clubs":10, "Ace of Clubs":11}

spades =   {"2 of Spades":2, "3 of Spades":3, "4 of Spades":4,
           "5 of Spades":5, "6 of Spades":6, "7 of Spades":7, 
           "8 of Spades":8, "9 of Spades":9, "10 of Spades":10,
           "Jack of Spades": 10, "Queen of Spades":10, 
           "King of Spades":10, "Ace of Spades":11}

# create list of suites for random choice
suites = [hearts, diamonds, clubs, spades]

# initialize list of player cards and list of player values
playerCards = []
playerValues = []

# initialize list of house cardss and house values
houseCards = []
houseValues = []

# get first two cards for player
for i in range(2):
    suite = choice(suites)
    card, value = choice(list(suite.items()))
    print(card)
    print(value)
    playerCards.append(card)
    playerValues.append(value)
    del suite[card]

# get first two cards for house
for i in range(2):
    suite = choice(suites)
    card, value = choice(list(suite.items()))
    print(card)
    print(value)
    houseCards.append(card)
    houseValues.append(value)
    del suite[card]

animatetext("""
Your cards: """ + printlist(playerCards) + """
              ----
Total Value:   """ + str(totalvalues(playerValues)) + """
              ----
--------------------------------
House cards: """ + houseCards[0] + """
             ? ? ?
              ----
Total Value:   ?
              ----
""")

#print("Spades \u2664")

while True:
    answer = input("Hit or Stay?: ")
    if answer.upper() == "STAY":
        playerVal = totalvalues(playerValues)
        houseVal = totalvalues(houseValues)
        if playerVal <= 21 and playerVal > houseVal:
            animatetext("""
Your cards: """ + printlist(playerCards) + """
              ----
Total Value:   """ + str(totalvalues(playerValues)) + """
              ----
--------------------------------
House cards: """ + printlist(houseCards) + """
              ----
Total Value:   """ + str(totalvalues(houseValues)) + """
              ----
""")
            print("You win! This time.")
            break
        else:
            animatetext("""
Your cards: """ + printlist(playerCards) + """
              ----
Total Value:   """ + str(totalvalues(playerValues)) + """
              ----
--------------------------------
House cards: """ + printlist(houseCards) + """
              ----
Total Value:   """ + str(totalvalues(houseValues)) + """
              ----
""")
            print("You lose :o")
            break
            

    elif answer.upper() == "HIT":
        suite = choice(suites)
        card, value = choice(list(suite.items()))
        print(card)
        print(value)
        playerCards.append(card)
        playerValues.append(value)
        del suite[card]
        suite = choice(suites)
        card, value = choice(list(suite.items()))
        print(card)
        print(value)
        houseCards.append(card)
        houseValues.append(value)
        del suite[card]
    
    animatetext("""
    Your cards: """ + printlist(playerCards) + """
                  ----
    Total Value:   """ + str(totalvalues(playerValues)) + """
                  ----
    --------------------------------
    House cards: """ + printlist(houseCards) + """
                  ----
    Total Value:   """ + str(totalvalues(houseValues)) + """
                  ----
    """)
