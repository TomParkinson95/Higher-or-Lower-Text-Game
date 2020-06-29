import time
import random


deck = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}


moves = ["higher", "lower"]

class Player:

    def __init__(self):
        self.score = 0
        self.picked_cards = []


    def move(self):
        move = ""
        while move not in moves:
            move = input("Higher or lower? >> ").lower()
        return move


def make_line(length, list):
    line = ""
    for i in range(length):
        line += str(list[i][0]) + " "
    return line + "\n"


def build_triangle(lines, list):
    triangle = ""
    i = lines
    while i > 0:
        triangle += make_line(i, list)
        i -= 1
    return triangle

def print_pause(msg):
    time.sleep(1)
    print(msg)


me = Player()
index = -1
while len(me.picked_cards) < 10:
    next_card = random.choice(list(deck.items()))
    if len(me.picked_cards) == 0:
        me.picked_cards.append(next_card)
        #print(make_line(len(me.picked_cards), me.picked_cards))
        index += 1
    else:
        print("Your cards:", make_line(len(me.picked_cards), me.picked_cards))
        print("Next card:", next_card)
        player_move = me.move()
        print("Player move was", player_move)
        if player_move == "higher" and me.picked_cards[index][1] < next_card[1]:
            print("Yes, it was higher. Well done!")
            me.picked_cards.append(next_card)
            index += 1
        elif player_move == "higher" and me.picked_cards[index][1] > next_card[1]:
            print(f"Oh no, it was {next_card[0]}! Start again!")
            me.picked_cards.clear()
            index = -1
        elif player_move in moves and me.picked_cards[index][1] == next_card[1]:
            print("Nuts, the card is the same! choosing another card for you =)")
        elif player_move == "lower" and me.picked_cards[index][1] > next_card[1]:
            print("Well done, it was lower!")
            me.picked_cards.append(next_card)
            index += 1
        else:
            print(f"Oh no, it was {next_card[0]}! Start again!")
            me.picked_cards.clear()
            index = -1
print("Your cards:\n", make_line(len(me.picked_cards), me.picked_cards))
print(build_triangle(4, me.picked_cards))


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
