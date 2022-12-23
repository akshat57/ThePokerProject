
# coding: utf-8

# In[5]:


'''
    Here we assign points to different poker hands. And also assign strength to the different hands
    Royal Flush = 10
    Straigh Flush = 9
    4 of a Kind = 8
    Full House = 7
    Flush = 6
    Straight = 5
    Three of a Kind = 4
    Two Pair = 3
    One Pair = 2
    High Card = 1
'''


# In[6]:


from PokerHands import *
import random


# In[7]:


class Check_Hand(NumberHands,SuiteAndSequenceHands):
    def __init__(self, Player, Table):
        self.number_hands = NumberHands(Player, Table)
        self.sas_hands = SuiteAndSequenceHands(Player, Table)
        #self.number_hands.Tell()
        #self.sas_hands.Tell()
        
        if self.sas_hands.royal_flush == True:
            self.points = 10
            self.high = self.sas_hands.straightflush_high
            self.next_high = None
        
        elif self.sas_hands.straight_flush == True:
            self.points = 9
            self.high = self.sas_hands.straightflush_high
            self.next_high = None
            
        elif self.number_hands.fourOfAKind == True:
            self.points = 8
            self.high = self.number_hands.most_frequent_card
            self.next_high = max(set(self.number_hands.all_cards) - set([self.number_hands.most_frequent_card]))
            
        elif self.number_hands.fullHouse == True:
            self.points = 7
            self.high = self.number_hands.most_frequent_card
            self.next_high = self.number_hands.next_most_frequent_card
            
        elif self.sas_hands.flush == True:
            self.points = 6
            self.high =  self.sas_hands.flush_high
            self.next_high = None#not included when class between flush high

        elif self.sas_hands.straight == True:
            self.points = 5
            self.high = self.sas_hands.straight_high
            self.next_high = None
            
        elif self.number_hands.threeOfAKind == True:
            self.points = 4
            self.high = self.number_hands.most_frequent_card
            self.next_high =  max(set(self.number_hands.all_cards) - set([self.number_hands.most_frequent_card]))
            
        elif self.number_hands.twopair == True:
            self.points = 3
            self.high = self.number_hands.most_frequent_card
            self.next_high = self.number_hands.next_most_frequent_card
            
        elif self.number_hands.pair == True:
            self.points = 2
            self.high = self.number_hands.most_frequent_card
            self.next_high = max(set(self.number_hands.all_cards) - set([self.number_hands.most_frequent_card]))
            
        else:
            self.points = 1
            self.high = self.number_hands.highcard
            self.next_high = max(set(self.number_hands.all_cards) - set([self.high]))
            
        
        #elif self


# In[8]:


def PointsToHand(points):
    if points == 10:
        return 'Royal Flush'
    elif points == 9:
        return 'Straigh Flush'
    elif points == 8:
        return 'Four of a Kind'
    elif points == 7:
        return 'Full House'
    elif points == 6:
        return 'Flush'
    elif points == 5:
        return 'Straight'
    elif points == 4:
        return 'Three of A Kind'
    elif points == 3:
        return 'Two Pairs'
    elif points == 2:
        return 'One Pair'
    else:
        return 'High Card'

