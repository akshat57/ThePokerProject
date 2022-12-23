
# coding: utf-8

# In[1]:


#Cards
'''
1-13 : Diamonds
14-26 : Hearts
27-39 : Clubs
40-52 : Spades
'''

###Functions defining card suite, card number, and card name/type

# In[2]:

class Card():
    def __init__(self, n):
        self.n = n

        #initialize cards
        self.suite = self.cardSuite(n)
        self.number = self.cardNumber(n)
        self.type = self.cardType(self.number)

    def cardSuite(self, n):
        suite = None

        if n >=1 and n <= 13:#Diamonds
            suite = 'Diamonds'
        elif n >=14 and n <= 26:
            suite = 'Hearts'
        elif n >=27 and n <= 39:
            suite = 'Clubs'
        elif  n >=40 and n <= 52:
            suite = 'Spades'

        return suite


    def cardNumber(self, n):
        number = None

        if n >= 1 and n <= 52:
            if n%13 != 0:
                number= n%13
            else:
                number = 13

        return number


    def cardType(self, n):
        card_type = None

        if n != None:
            if n == 1:
                card_type = 'Ace'
            elif n >= 2 and n <= 10:
                card_type = str(n)
            elif n == 11:
                card_type = 'Jack'
            elif n == 12:
                card_type = 'Queen'
            elif n == 13:
                card_type = 'King'

        return card_type


if __name__ == '__main__':

    for i in range(0, 54):
        card = Card(i)
        print(i, card.suite, card.number, card.type)