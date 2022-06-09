# nickname generator
# (could also be used for musician name generator, etc)
from random import choice
from termcolor import colored
from random import randint

word1 = [
        "alert", "clumsy", "blue-eyed", "determined", 
        "expensive", "modern", "powerful", "successful", 
        "strange", "talented", "tough", "zany", "immense", 
        "muscular", "fancy", "witty", "ancient", 
        "friendly", "elderly", "wise"
        ]

word2 = [
        "roadrunner", "sunlight", "flower", "librarian", 
        "sea-salt", "machine", "shakespeare", "skyscraper", 
        "internet", "foot", "coder", "chef", "expert", 
        "theory", "law", "army", "child", "unit", "boss", 
        "program"
        ]

word3 = [
        "of justice", "the third", "junior", "the mystical", 
        "the wise", "the strong", "undercover", "by foot",
        ]

while True:
    name = input("Enter your name to receive your new nickname: ")
    

    while len(name.split(" ")) < 2:
        name = input("Enter at least your first and last name. Middle initial optional. ")

    name = name.split(" ")

    name[0] = choice(word1)
    name[1] = choice(word2)
    new_name = name[0] + " " + name[1]

    rand_number = randint(1, 10)
    if rand_number > 7:
        name.append(choice(word3))
        new_name = new_name + " " + name[2]

    print("From now on, you shall be known as: ")
    print(colored(new_name, "red"))

    again = input("Do you require another nickname? y/n: ")
    
    if again == "n":
        print("Farewell, " + colored(new_name, "red"))
        break
    else:
        print("Very well...")