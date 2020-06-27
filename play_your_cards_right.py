import random

deck_cards = {
  "hearts": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]",
  "spades": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]",
  "diamonds": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]",
  "clubs": "[2,3,4,5,6,7,8,9,10,J,Q,K,A]"
}

for key in deck_cards.keys():
    print(key)

#
# first - we need to generate ten random cards from the dictionary (or list?)
#
#
# the game should give an output at the beginning like this (to represent the cards):
#
#   ####
#    ###
#     ##
#      #
# each of these represent a card. as a card is turned over, mark it with 0:
#
#   00##
#    ###
#     ##
#      #
#
#
#
