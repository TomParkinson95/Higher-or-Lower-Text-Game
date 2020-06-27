import random
import time


deck_cards = {
  "hearts": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]",
  "spades": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]",
  "diamonds": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]",
  "clubs": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]"
}

test_deck = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14


}

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]


class Player:

    def __init__(self):
        self.score = 0


    def move(self):
        return input("Higher or lower?").lower()




game_deck = []

for i in range(10):
    print(random.choice(deck))
    game_deck.append(random.choice(deck))

game_deck.sort()

print(game_deck)

#for key in deck_cards.keys():
#    print(key)

#for list in list_cards:
#    print(list[random.randint(0, len(list)-1)])
    #print(len(list))

#
# first - we need to generate ten random cards from the dictionary (or list?)
#
#
# the game should give an output at the beginning like this (to represent the cards):
#
#   # # # #
#     # # #
#       # #
#         #
# each of these represent a card. as a card is turned over, mark it with the indicator:
#
#   K Q 8 #
#     # # #
#       # #
#         #
#
#
#
