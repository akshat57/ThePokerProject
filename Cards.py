
# coding: utf-8

# In[1]:


#Cards
'''
1-13 : Diamonds
14-26 : Hearts
27-39 : Clubs
40-52 : Spades
'''


# In[2]:


class CardSuite():
    def __init__(self, n):
        if n < 1 or n > 52:
            self.suite = None
        else:
            if n//13 == 0 or (n//13 == 1 and n%13 == 0):#Diamonds
                self.suite = 'Diamonds'
            elif n//13 == 1 or (n//13 == 2 and n%13 == 0):#Diamonds
                self.suite = 'Hearts'
            elif n//13 == 2 or (n//13 == 3 and n%13 == 0):#Diamonds
                self.suite = 'Clubs'
            else: 
                self.suite = 'Spades'
            
    def suite(self):
        return self.suite
        


# In[3]:


class CardNumber():
    def __init__(self, n):
        if n < 1 or n > 52:
            self.card = None
        else:
            if n%13 != 0:
                self.card = n%13
            else:
                self.card = 13
                
    def card(self):
        return self.card

        


# In[4]:


class CardType():
    def __init__(self, n):
        if n < 1 or n > 13:
            self.type = None
        else:
            if n == 1:
                self.type = 'Ace'
            elif n == 2:
                self.type = '2'
            elif n == 3:
                self.type = '3'
            elif n == 4:
                self.type = '4'
            elif n == 5:
                self.type = '5'
            elif n == 6:
                self.type = '6'
            elif n == 7:
                self.type = '7'
            elif n == 8:
                self.type = '8'
            elif n == 9:
                self.type = '9'
            elif n == 10:
                self.type = '10'
            elif n == 11:
                self.type = 'Jack'
            elif n == 12:
                self.type = 'Queen'
            elif n == 13:
                self.type = 'King'
                
    def cardtype(self):
        return self.type
                

