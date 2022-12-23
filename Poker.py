
# coding: utf-8

# In[8]:


'''
    Here, classes for PokerPlayer and the PokerTable are defined.
    PokerPlayer contains the cards for the poker player
    PokterTable contains the cards for the poker table
'''


# In[9]:


from Cards import Card
import random


# In[2]:


class PokerPlayer(Card):
    def __init__(self, n1, n2):
        if n1 == n2:#initializaing everything to None
            self.card1 = Card(0)
            self.card2 = Card(0)
            self.valid = False
        else:
            self.card1 = Card(n1)
            self.card2 = Card(n2)
            self.valid = True
        
    def show_types(self):
        return [ (self.card1.type, self.card1.suite), (self.card2.type, self.card2.suite) ]
    
    def show_cards(self):
        return [ (self.card1.number, self.card1.suite), (self.card2.number, self.card2.suite) ]
    
    def all_suites(self):
        return [self.card1.suite, self.card2.suite]

    def all_cards(self):
        return [self.card1.number, self.card2.number]
       

# In[3]:


class PokerTable(Card):
    def __init__(self, n1, n2, n3, n4, n5):#in order of appearence
        if len(set([n1, n2, n3, n4, n5])) != 5:
            self.card1, self.card2, self.card3, self.card4, self.card5 = Card(0), Card(0), Card(0), Card(0), Card(0)
            self.valid = False
        else:
            self.card1 = Card(n1)
            self.card2 = Card(n2)
            self.card3 = Card(n3)
            self.card4 = Card(n4)
            self.card5 = Card(n5)
            self.valid = True
        
    def show_types(self):
        return [(self.card1.type, self.card1.suite), (self.card2.type, self.card2.suite), (self.card3.type, self.card3.suite), (self.card4.type, self.card4.suite), (self.card5.type, self.card5.suite)]

    def show_cards(self):
        return [(self.card1.number, self.card1.suite), (self.card2.number, self.card2.suite), (self.card3.number, self.card3.suite), (self.card4.number, self.card4.suite), (self.card5.number, self.card5.suite)]
    
    def all_suites(self):
        return [self.card1.suite, self.card2.suite, self.card3.suite, self.card4.suite, self.card5.suite]
    
    def all_cards(self):
        return [self.card1.number, self.card2.number, self.card3.number, self.card4.number, self.card5.number]
        
    

if __name__ == '__main__':

    ##Checking Poker Player
    player = PokerPlayer(42, 42)
    print(player.show_cards(), player.show_types(), player.all_suites())
    for i in range(5):
        player = PokerPlayer(random.randint(1,52), random.randint(1,52))
        print(i, player.show_cards(), player.show_types(), player.all_suites(), player.all_cards())

    print('\n', '-'*50, '\n')

    ##Checking PokerTable
    table = PokerTable(42, 42, 42, 42, 42)
    print(table.show_cards(), table.show_types(), table.all_suites(), table.all_cards())
    for i in range(5):
        table = PokerTable(random.randint(1,52), random.randint(1,52), random.randint(1,52), random.randint(1,52), random.randint(1,52))
        print(i, table.show_cards(), table.show_types(), table.all_suites(), table.all_cards())