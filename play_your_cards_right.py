import random
import time


deck_cards = {
  "hearts": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]",
  "spades": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]",
  "diamonds": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]",
  "clubs": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]"
}

test_deck = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

ten_decks = [
    [2,3,4,5,6,7,8,9,10,11,12,13,14],
    [2,3,4,5,6,7,8,9,10,11,12,13,14],
    [2,3,4,5,6,7,8,9,10,11,12,13,14],
    [2,3,4,5,6,7,8,9,10,11,12,13,14],
    [2,3,4,5,6,7,8,9,10,11,12,13,14],
    [2,3,4,5,6,7,8,9,10,11,12,13,14],
    [2,3,4,5,6,7,8,9,10,11,12,13,14],
    [2,3,4,5,6,7,8,9,10,11,12,13,14],
    [2,3,4,5,6,7,8,9,10,11,12,13,14],
    [2,3,4,5,6,7,8,9,10,11,12,13,14]
]

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]

moves = ["higher", "lower"]

class Player:

    def __init__(self):
        self.score = 0


    def move(self):
        move = ""
        while move not in moves:
            move = input("Higher or lower? >> ").lower()
        return move




game_deck = [] # deck that is laid out for the player when game starts- needed?

picked_cards = [] # stores the cards the player already picked

me = Player()
index = -1
while len(picked_cards) < 10:
    #next_card = random.randint(0, len(deck)-1)
    next_card = random.choice(deck)
    if len(picked_cards) == 0:
        picked_cards.append(next_card)
        print("Picked cards:", picked_cards)
        index += 1
    else:
        print("Picked cards: ", picked_cards)
        print("Next card:", next_card)
        player_move = me.move()
        print("Player move was ", player_move)
        if player_move == "higher" and picked_cards[index] < next_card:
            print("Yes, it was higher. Well done!")
            picked_cards.append(next_card)
            index += 1
        elif player_move == "higher" and picked_cards[index] > next_card:
            print("Oh no, bad luck! Start again!")
            picked_cards.clear()
            index = -1
        elif player_move in moves and picked_cards[index] == next_card:
            print("Nuts, the card is the same! choosing another card for you =)")
        elif player_move == "lower" and picked_cards[index] > next_card:
            print("Well done, it was lower!")
            picked_cards.append(next_card)
            print(picked_cards)
            index += 1
        else:
            print("Oh no, it was higher! Start again!")
            picked_cards.clear()
            index = -1
# add a few more elif statements, so that the game knows what to do if the
# player chose wrongly (eg they pick lower but the next card was higher)
# use list.clear() to empty the list if they get a card wrong.

# game_deck.sort()
# print(game_deck)


# for list in ten_decks:
#     random.shuffle(list)
#     game_deck.append(random.choice(list))

# for i in range(10):
#     rand_card = random.choice(deck)
#     if game_deck[i] != rand_card:
#         game_deck.append(random.choice(deck))

# game_deck.append(random.choice(deck))
# index = 0
# while len(game_deck) < 10:
#     rand_card = random.choice(deck)
#     if game_deck[index] != rand_card:
#         game_deck.append(rand_card)
#     else:
#
#     index += 1





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
