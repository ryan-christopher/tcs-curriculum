import random


def makeDeck():
    deck = []
    c = 0
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

    for v in values:
        for s in suits:
            deck.append([v,s])

    random.shuffle(deck)

    return deck

deck = makeDeck()

player = []

cpu = []

for i in range(5):
    card = random.choice(deck)
    deck.remove(card)
    player.append(card)
    card = random.choice(deck)
    deck.remove(card)
    cpu.append(card)


print(player)
print(cpu)