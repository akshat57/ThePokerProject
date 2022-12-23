#here I want to calculate generate stats about what kind of hands usually win in a poker game

from PokerHands import *
from PokerRules import *
from PokerGame import *
import random

all_cards = [i for i in range(1,53)]
heros_hand = random.sample(all_cards, 2)
num_players = 9

myGame = Game(heros_hand, num_players)
print(myGame.split, myGame.winning_hand)
print(myGame.Show_Game())
