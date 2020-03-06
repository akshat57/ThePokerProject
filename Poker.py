
# coding: utf-8

# In[8]:


'''
    Here, classes for PokerPlayer and the PokerTable are defined.
    PokerPlayer contains the cards for the poker player
    PokterTable contains the cards for the poker table
'''


# In[9]:


from Cards import *


# In[2]:


class PokerPlayer(CardSuite, CardNumber, CardType):
    def __init__(self, n1, n2):
        self.card1 = CardNumber(n1).card
        self.type1 = CardType(self.card1).cardtype()
        self.suite1 = CardSuite(n1).suite

        
        self.card2 = CardNumber(n2).card
        self.type2 = CardType(self.card2).cardtype()
        self.suite2 = CardSuite(n2).suite
        
    def show_types(self):
        return [ (self.type1, self.suite1), (self.type2, self.suite2) ]
    
    def show_cards(self):
        return [ (self.card1, self.suite1), (self.card2, self.suite2) ]
    
    def all_suites(self):
        return [self.suite1, self.suite2]


# In[3]:


class PokerTable(CardSuite, CardNumber, CardType):
    def __init__(self, n1, n2, n3, n4, n5):#in order of appearence
        self.card1 = CardNumber(n1).card
        self.type1 = CardType(self.card1).cardtype()
        self.suite1 = CardSuite(n1).suite

        self.card2 = CardNumber(n2).card
        self.type2 = CardType(self.card2).cardtype()
        self.suite2 = CardSuite(n2).suite
        
        self.card3 = CardNumber(n3).card
        self.type3 = CardType(self.card3).cardtype()
        self.suite3 = CardSuite(n3).suite
        
        self.card4 = CardNumber(n4).card
        self.type4 = CardType(self.card4).cardtype()
        self.suite4 = CardSuite(n4).suite
        
        self.card5 = CardNumber(n5).card
        self.type5 = CardType(self.card5).cardtype()
        self.suite5 = CardSuite(n5).suite
        
    def show_types(self):
        return [(self.type1, self.suite1), (self.type2, self.suite2), (self.type3, self.suite3), (self.type4, self.suite4), (self.type5, self.suite5)]

    def show_cards(self):
        return [(self.card1, self.suite1), (self.card2, self.suite2), (self.card3, self.suite3), (self.card4, self.suite4), (self.card5, self.suite5)]
    
    def all_suites(self):
        return [self.suite1, self.suite2, self.suite3, self.suite4, self.suite5]
    
    def all_cards(self):
        return [self.card1, self.card2, self.card3, self.card4, self.card5]
        
    

