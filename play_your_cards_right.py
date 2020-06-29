import time
import random

# Dictionary used for drawing cards.
deck = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "X": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}


class Player:

    def __init__(self):
        self.score = 0
        self.picked_cards = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        self.moves = ["higher", "lower"]
        self.num_moves = 0


    def move(self):
        move = ""
        while move not in self.moves:
            move = input("Higher or lower? >> ").lower()
        return move

# RandomPlayer class for testing purposes.
class RandomPlayer(Player):

    def move(self):
        return random.choice(self.moves)

# The three functions immediately below this comment MAY be deprecated.
def make_line_dict(length, dict):
    line = ""
    for key in dict.keys():
        line += key + " "
    return line + "\n"


def build_triangle_dict(lines, dict):
    triangle = ""
    i = lines
    while i > 0:
        triangle += make_line_dict(i, dict)
        i -= 1
    return triangle


def make_line(length, list):
    line = ""
    for i in range(length):
        line += str(list[i][0]) + " "
    return line + "\n"

# Gives the nice card layout.
def build_triangle(list):
    triangle = ("{:3} {:3} {:3} {:3}\n\n"
                "{:3} {:3} {:3}\n\n"
                "{:3} {:3}\n\n"
                "{:3}\n".format(list[0][0], list[1][0], list[2][0], list[3][0],
                                list[4][0], list[5][0], list[6][0], list[7][0],
                                list[8][0], list[9][0]))
    # i = lines
    # while i > 0:
    #     triangle += make_line(i, list)
    #     i -= 1
    return triangle


# Prints a message and gives a delay.
def print_pause(msg):
    time.sleep(0.0000000000000075)
    print(msg)


def outro(num_moves):
    if num_moves < 15:
        print_pause(f"Congratulations, you completed the game in {num_moves}"
                    " moves, you win £10,000!")
    elif num_moves < 20:
        print_pause(f"Congratulations, you completed the game in {num_moves}"
                    " moves, you win £5,000!")
    elif num_moves < 30:
        print_pause(f"Congratulations, you completed the game in {num_moves}"
                    " moves, you win £1,000!")
    elif num_moves < 50:
        print_pause(f"Congratulations, you completed the game in {num_moves}"
                    " moves, you win this lovely 'Took part' medal!")
        print_pause("SMACK!")
        print_pause("Umm... ouch. Thanks for playing!")
    else:
        print_pause("Hmmm... are you some random robot from Python 3 pretending to be a human?")
        print_pause("We can sue you for that you know...")
        print_pause("Wait... huh? What are you doing? Please don't hurt me!")
        print_pause("We can give you all the money! Lots of money! Anything you want!")
        print_pause("ZZZZZZZZ!")
        print_pause("ARGH NOOOOOO!")


def play_again():
    ans = input("Would you like to play again [y/n]? >> ")
    if ans == "n":
        print_pause("Thanks for joining us, goodbye!")
    elif ans == "y":
        print_pause("Lovely! Welcome back!")
        play_game()
    else:
        print_pause("Please choose a valid answer.")
        play_again()


def play_game():
    print_pause("Good evening and welcome to Play Your Cards Right, "
                "with your favourite host....")
    print_pause("Brrruuuuuuccceeeeeee Forsyth!")
    # Change the below to whichever class you want to use.
    me = RandomPlayer()
    index = -1
    while me.picked_cards[9] == "#":
        next_card = random.choice(list(deck.items()))
        if me.picked_cards[0] == "#":
            me.picked_cards.remove("#")
            index += 1
            me.picked_cards.insert(index, next_card)
        else:
            print_pause("Your cards:\n\n" + build_triangle(me.picked_cards))
            #print("Next card:", next_card)
            player_move = me.move()
            print_pause(f"You chose {player_move}! Let's see if you were right!")
            if player_move == "higher" and me.picked_cards[index][1] < next_card[1]:
                print_pause(f"It was a {next_card[0]}! Well done!")
                me.picked_cards.remove("#")
                me.picked_cards.insert(index + 1, next_card)
                index += 1
            elif player_move == "higher" and me.picked_cards[index][1] > next_card[1]:
                print_pause(f"Oh no, it was {next_card[0]}! Start again!")
                me.picked_cards = ["#", "#", "#", "#", "#",
                                   "#", "#", "#", "#", "#"]
                index = -1
            elif player_move in me.moves and me.picked_cards[index][1] == next_card[1]:
                print_pause(f"Wow - the card was also a {next_card[0]}! Choosing another...")
            elif player_move == "lower" and me.picked_cards[index][1] > next_card[1]:
                print_pause(f"Well done, it was a {next_card[0]}!")
                me.picked_cards.remove("#")
                me.picked_cards.insert(index + 1, next_card)
                index += 1
            else:
                print_pause(f"Oh no, it was {next_card[0]}! Start again!")
                me.picked_cards = ["#", "#", "#", "#", "#",
                                   "#", "#", "#", "#", "#"]
                index = -1
        me.num_moves += 1
    print(build_triangle(me.picked_cards))
    print_pause("Moves taken to win: " + str(me.num_moves))
    # Different win conditions.
    outro(me.num_moves)
    play_again()


play_game()

# print(build_triangle(4, player_deck))
# print(make_line(len(player_deck), player_deck))
# print(len(player_deck), len(deck))
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
