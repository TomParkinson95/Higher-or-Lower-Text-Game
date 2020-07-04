# Play Your Cards Right, Copyright Tom Parkinson 2020.
import time
import random
from colorama import Fore, Back, Style


# The below is backup of the deck variable in case the card symbols don't work.
# deck = {
#     "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
#     "X": 10, "J": 11, "Q": 12, "K": 13, "A": 14
# }


# Default Player class, which is used by a human player.
class Player:

    def __init__(self):
        self.picked_cards = ["🂠", "🂠", "🂠", "🂠", "🂠", "🂠", "🂠", "🂠",
                             "🂠", "🂠"]
        self.moves = ["higher", "lower"]
        self.num_moves = 0

    def move(self, card):
        move = ""
        while move not in self.moves:
            move = input(Fore.RED + "Higher or lower than"
                                  + f" {check_vowels(card)} "
                                  + f"{check_values(card)}? >> ").lower()
        return move


# RandomPlayer class for testing purposes.
class RandomPlayer(Player):

    def move(self, card):
        print(Fore.RED + "Higher or lower than "
                       + f"{check_vowels(card)} {check_values(card)}?")
        return random.choice(self.moves)


# CyclePlayer - different playing stategy - cycles through all moves.
class CyclePlayer(Player):

    def __init__(self):
        super().__init__()
        self.last_move = ""

    def move(self, card):
        if self.last_move == "":
            move = random.choice(self.moves)
            self.last_move = move
            print(Fore.RED + "Higher or lower than "
                           + f"{check_vowels(card)} {check_values(card)}?")
            return move
        else:
            if self.last_move == "higher":
                print(Fore.RED + "Higher or lower than "
                               + f"{check_vowels(card)} {check_values(card)}?")
                self.last_move = "lower"
                return "lower"
            elif self.last_move == "lower":
                print(Fore.RED + f"Higher or lower than "
                               + f"{check_vowels(card)} {check_values(card)}?")
                self.last_move = "higher"
                return "higher"


# Check the values higher than 10 and return the appropriate letter.
def check_values(card):
    card = list(card)
    if card[1] > 10:
        return ['J', 'Q', 'K', 'A'][card[1] - 11]
    else:
        return str(card[1])


# Checks the key of the card and determines whether to use "a" or "an".
def check_vowels(card):
    # input(f"In check vowels, the card is: {card}") <- debug for check_vowels
    return 'a' + 'n' * (card[1] in [8, 14])


# Gives the nice card layout.
# String layout as used in the function is to help visualise how the cards
# will be printed.
def build_triangle(list):
    return "{:3} {:3} {:3} {:3}\n\n"
            + "    {:3} {:3} {:3}\n\n"
            + "        {:3} {:3}\n\n"
            + "            {:3}\n".format(list[0][0], list[1][0], list[2][0],
                                        list[3][0], list[4][0], list[5][0],
                                        list[6][0], list[7][0], list[8][0],
                                        list[9][0])


# Prints a message and gives a delay.
def print_pause(msg):
    time.sleep(0.75)
    print(msg)


def outro(num_moves):
    if num_moves < 20:
        print_pause(f"Congratulations, you completed the game in {num_moves}"
                    " moves, you win £10,000!")
    elif num_moves < 25:
        print_pause(f"Congratulations, you completed the game in {num_moves}"
                    " moves, you win £5,000!")
    elif num_moves < 35:
        print_pause(f"Congratulations, you completed the game in {num_moves}"
                    " moves, you win £1,000!")
    elif num_moves < 100:
        print_pause(f"Congratulations, you completed the game in {num_moves}"
                    " moves, you win this lovely 'Took part' medal!")
        print_pause("SMACK!")
        print_pause("Umm... ouch. Thanks for playing!")
    elif num_moves < 600:
        print_pause(f"{num_moves} moves... okay "
                    "this is a little suspicious...")
        print_pause("Are you a Cycle robot from Python 3?")
        print_pause("Zzzzzzt.")
        print_pause("#Pedalling sound#")
        print_pause("NOOO PLEASE DON'T CYCLE OVER MEEEE!")
        print_pause("AARRRGGHHHH NOOOOOOOO!")
    else:
        print_pause(f"{num_moves} moves? Hmmm... are you some random robot "
                    "from Python 3 pretending to be a human?")
        print_pause("We can sue you for that you know...")
        print_pause("Wait... huh? What are you doing? Please don't hurt me!")
        print_pause("We can give you all the money! Lots of money!"
                    " Anything you want!")
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
    # Dictionary used for drawing cards, in order: spades/hearts/diamonds/clubs
    deck = {
        "🂢": 2, "🂣": 3, "🂤": 4, "🂥": 5, "🂦": 6, "🂧": 7, "🂨": 8, "🂩": 9,
        "🂪": 10, "🂫": 11, "🂭": 12, "🂮": 13, "🂡": 14,
        "🂲": 2, "🂳": 3, "🂴": 4, "🂵": 5, "🂶": 6, "🂷": 7, "🂸": 8, "🂹": 9,
        "🂺": 10, "🂻": 11, "🂽": 12, "🂾": 13, "🂱": 14,
        "🃂": 2, "🃃": 3, "🃄": 4, "🃅": 5, "🃆": 6, "🃇": 7, "🃈": 8, "🃉": 9,
        "🃊": 10, "🃋": 11, "🃍": 12, "🃎": 13, "🃁": 14,
        "🃒": 2, "🃓": 3, "🃔": 4, "🃕": 5, "🃖": 6, "🃗": 7, "🃘": 8, "🃙": 9,
        "🃚": 10, "🃛": 11, "🃝": 12, "🃞": 13, "🃑": 14
    }
    blank_deck = ["🂠", "🂠", "🂠", "🂠", "🂠", "🂠", "🂠", "🂠", "🂠", "🂠"]
    print(Fore.RED)
    print(Back.WHITE)
    print_pause("Good evening and welcome to Play Your Cards Right, "
                "with your favourite host....")
    print_pause("Brrruuuuuuccceeeeeee Forsyth!")
    # Change the below to whichever class you want to use.
    me = Player()
    index = -1
    while me.picked_cards[9] == "🂠":
        next_card = list(random.choice(list(deck.items())))
        if me.picked_cards[0] == "🂠":
            me.picked_cards.remove("🂠")
            index += 1
            me.picked_cards.insert(index, next_card)
        else:
            print_pause("Your cards:\n\n" + Fore.BLACK +
                        build_triangle(me.picked_cards))
            # print(Fore.RED + "Next card:", next_card) # Debug statement <-
            player_move = me.move(me.picked_cards[index])
            print_pause(f"You chose {player_move}!"
                        " Let's see if you were right!")
            # print(f"The value of the card before checking it's value is:
            # {next_card}") # debug card before checking value
            if (player_move == "higher" and
               me.picked_cards[index][1] < next_card[1]):
                print_pause(f"It was {check_vowels(next_card)}"
                            f" {check_values(next_card)}!"
                            " Well done!")
                me.picked_cards.remove("🂠")
                me.picked_cards.insert(index + 1, next_card)
                index += 1
            elif (player_move == "higher" and
                  me.picked_cards[index][1] > next_card[1]):
                print_pause(f"Oh no, it was {check_vowels(next_card)}"
                            f" {check_values(next_card)}! Start again!")
                me.picked_cards.clear()
                me.picked_cards = blank_deck.copy()
                # input(f"The player deck when losing on higher is :
                # {me.picked_cards}") <- debugs loss condition
                index = -1
            elif (player_move in me.moves and
                  me.picked_cards[index][1] == next_card[1]):
                me.num_moves -= 1
                print_pause("Wow - the card was also "
                            f"{check_vowels(next_card)} "
                            f"{check_values(next_card)}!"
                            " Choosing another...")
            elif (player_move == "lower" and
                  me.picked_cards[index][1] > next_card[1]):
                print_pause(f"Well done, it was {check_vowels(next_card)} "
                            f"{check_values(next_card)}!")
                me.picked_cards.remove("🂠")
                me.picked_cards.insert(index + 1, next_card)
                index += 1
            else:
                print_pause(f"Oh no, it was {check_vowels(next_card)} "
                            f"{check_values(next_card)}! Start again!")
                me.picked_cards.clear()
                me.picked_cards = blank_deck.copy()
                # input(f"The player deck when losing on lower is :
                # {me.picked_cards}") <- debugs loss condition
                index = -1
        me.num_moves += 1
    print_pause(Fore.RED + "You won! Here are your cards:\n\n" +
                Fore.BLACK + build_triangle(me.picked_cards))
    print_pause(Fore.RED + "Moves taken to win: " + str(me.num_moves))
    # Different win conditions are call based on the value of me.num_moves.
    outro(me.num_moves)
    play_again()


play_game()


# Currently the cards are displayed with right alignment, as below.
#
#   # # # #
#     # # #
#       # #
#         #
# as a card is turned over, it is marked with the drawn card:
#
#   K Q 8 #
#     # # #
#       # #
#         #
