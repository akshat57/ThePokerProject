
# coding: utf-8

# In[49]:


'''
    We divide Hands into two types - NumberHands and SuiteAndSequenceHands
    NumberHands: High Card, Pair, Two Pair, Three of a Kind, Four of a Kind, Full House
    SuiteAndSequenceHands: Straight, Flush, Straight Flush, Royal Flush 

'''

####CORRECTION NEEDED
##Hand calculation is probably correct. But hand ranking needs to be improved. 
##This is for cases when we compare the same type of winning hand, like two pair vs two pair. We have to rank the top 5 cards in order
##So a separate function needs to be written for best 5 cards and then to rank them while choosing the winner.


# In[50]:


from Poker import *
from statistics import mode
from operator import itemgetter
import random


# In[51]:


class NumberHands():
    '''
    This class identifies: 
    High Card, Pair, Two Pair, Three of a Kind, Four of a Kind, Full House
    '''
    def __init__(self, player, table):
        self.most_frequent_card = None
        self.next_most_frequent_card = None

        card_set = set([player.card1.n, player.card2.n, table.card1.n, table.card2.n, table.card3.n, table.card4.n, table.card5.n])

        if player.valid and table.valid and len(card_set) == 7:
            self.valid_game = True
            self.All_Cards(player, table)
            self.Frequency()
            
            #check for hands
            self.highcard = self.Check_HighCard(player, table)
            self.pair = self.Check_Pair(player, table)
            self.twopair = self.Check_TwoPair(player, table)
            self.threeOfAKind = self.Check_ThreeOfAKind(player, table)
            self.fourOfAKind = self.Check_FourOfAKind(player, table)
            self.fullHouse = self.Check_FullHouse()
        else:
            self.valid_game = False
        
    
    def Tell(self):
        if self.valid_game:
            print('HighCard = ', self.highcard)
            print('Pair = ', self.pair, '\nTwoPair = ', self.twopair, '\nThree of a Kind = ', self.threeOfAKind , '\nFourofAKinds = ', self.fourOfAKind, '\nFullHouse = ', self.fullHouse  )
            print('Most Frequent Card:', self.most_frequent_card, 'Next most freq', self.next_most_frequent_card)
        else:
            print('INVALID GAME')

        

    def All_Cards(self, player, table):
        #accumulates all 7 cards for each player. Input is playerhand and tablecards
        Hand = player.show_cards() + table.show_cards()
        self.all_cards = []
        
        for (card, suite) in Hand:
            self.all_cards.append(card)

            
    def Frequency(self):
        #counting card frequencies for different hands

        self.card_frequency= {}#measures card frequency
        
        for card in self.all_cards:
            if card == 1:
                card = 14

            if card not in self.card_frequency.keys():
                self.card_frequency[card] = 1
            else:
                self.card_frequency[card] += 1        
        
        self.card_frequency = dict(sorted(self.card_frequency.items(), key=itemgetter(1), reverse = True))
        self.most_frequent_card = list(self.card_frequency.keys())[0]
        self.next_most_frequent_card = list(self.card_frequency.keys())[1]
        if len(self.card_frequency) > 2:
            self.third_most_frequent_card = list(self.card_frequency.keys())[2]
        else:
            self.third_most_frequent_card = 0

        #storing larger of the two pairs and two triplets as most frequent card.
        if self.card_frequency[self.most_frequent_card] == 2 and self.card_frequency[self.next_most_frequent_card] == 2:
            temp = sorted([self.most_frequent_card, self.next_most_frequent_card], reverse=True)
            self.most_frequent_card = temp[0]
            self.next_most_frequent_card = temp[1]

        elif self.card_frequency[self.most_frequent_card] == 2 and self.card_frequency[self.next_most_frequent_card] == 2 and self.card_frequency[self.third_most_frequent_card] == 2:
            temp = sorted([self.most_frequent_card, self.next_most_frequent_card, self.third_most_frequent_card], reverse=True)
            self.most_frequent_card = temp[0]
            self.next_most_frequent_card = temp[1]

        elif self.card_frequency[self.next_most_frequent_card] == 2 and self.third_most_frequent_card and self.card_frequency[self.third_most_frequent_card] == 2:
            temp = sorted([self.next_most_frequent_card, self.third_most_frequent_card], reverse=True)
            self.next_most_frequent_card = temp[0]

        elif self.card_frequency[self.most_frequent_card] == 3 and self.card_frequency[self.next_most_frequent_card] == 3:
            temp = sorted([self.most_frequent_card, self.next_most_frequent_card], reverse=True)
            self.most_frequent_card = temp[0]
            self.next_most_frequent_card = temp[1]
            
    
    def Check_HighCard(self, player, table):
        self.high_card = max(self.card_frequency)
        return self.high_card
    
    def Check_Pair(self, player, table):
        if self.card_frequency[self.most_frequent_card] >= 2:
            return True
        else:
            return False
        
        
    def Check_TwoPair(self, player, table):
        if (self.card_frequency[self.most_frequent_card] >= 2) and (self.card_frequency[self.next_most_frequent_card] >= 2):
            return True
        else:
            return False
        

    def Check_ThreeOfAKind(self, player, table):      
        '''To be called after Check_Pair'''
        
        if self.card_frequency[self.most_frequent_card] >= 3:
            return True
        else:
            return False
        
    
    def Check_FourOfAKind(self, player, table):
        '''Should be called after Check_Pair and three of a Check_ThreeOfAKind'''

        if self.card_frequency[self.most_frequent_card] == 4:
            return True
        else:
            return False
        
    def Check_FullHouse(self):
        if self.twopair == True and self.threeOfAKind == True:
            return True
        else:
            return False
        
    
 


# In[52]:


class SuiteAndSequenceHands():
    def __init__(self, player, table):
        self.straight_high = None
        self.flush_high = None
        self.straightflush_high = None
        self.most_frequent_suite = None
        card_set = set([player.card1.n, player.card2.n, table.card1.n, table.card2.n, table.card3.n, table.card4.n, table.card5.n])

        if player.valid and table.valid and len(card_set) == 7:
            self.valid_game = True
            self.All_Cards(player, table)
            
            self.straight = self.Check_Straight(player, table)
            self.flush = self.Check_Flush(player, table)
            self.straight_flush = self.Check_StraightFlush(player, table)
            self.royal_flush = self.Check_RoyalFlush()
        else:
            self.valid_game = False
            
        
    def Tell(self):
        if self.valid_game:
            print('Straight = ', self.straight, '\nFlush = ', self.flush, '\nStraightFlush = ', self.straight_flush, '\nRoyalFlush = ', self.royal_flush)
            print('Straigh high:', self.straight_high, '| Flush Suite:', self.most_frequent_suite, '| Flush high:', self.flush_high, '| StraightFlushHigh:', self.straightflush_high)
        else:
            print('INVLID GAME')
    
    def All_Cards(self, player, table):
        Hand = player.show_cards() + table.show_cards()
        self.all_cards = []
        
        for (card, suite) in Hand:
            self.all_cards.append(card)
        
    
    def Check_Straight(self, player, table):        
        cards = list(set(self.all_cards))
        cards.sort()
        result = self.Check_Sequence_Straight(cards)
        flag = result[0]
        if flag == True:
            self.straight_high = result[1]
        
        return flag
    
    
    def Check_Flush(self, player, table):
        suites = player.all_suites() + table.all_suites()
        self.most_frequent_suite = max(set(suites), key = suites.count)
    
        if suites.count(self.most_frequent_suite) >= 5:
            Hand = player.show_cards() + table.show_cards()
            self.sf_cards = [] # cards for flush
            
            for (card, suite) in Hand:
                if suite == self.most_frequent_suite:
                    self.sf_cards.append(card)
            
            self.sf_cards.sort()
            
            if min(self.sf_cards) == 1:
                self.flush_high = 14
            else:
                self.flush_high = max(self.sf_cards)
            
            return True
        else:
            return False
        
        
    def Check_StraightFlush(self, player, table):##Also Checks for royal Flush
        if self.flush == True:
            result = self.Check_Sequence_Straight(self.sf_cards)
            flag = result[0]
            if flag == True:
                self.straightflush_high = result[1]
            
            return flag
        
        else:
            return False
        
        
    def Check_RoyalFlush(self):
        if self.straight_flush == True:
            if self.straightflush_high == 14:
                return True
                
        return False
        
    
        
    def Check_Sequence_Straight(self, sequence):
        '''
        Input: A sorted list of numbers with NO REPITITION. Sorting from low to high (increasing order)
        Output: [Flag, Straight High Card]
                where Flag = True if there is a straight and False if not. High Card represent straight high
        '''

        if len(sequence) < 5:
            return [False, None]
        
        elif len(sequence) == 5:
            if max(sequence) - min(sequence) == 4:
                return [True, max(sequence)]
                
            elif sequence[0] == 1:
                new_sequence = sequence[1:] + [14]
                if max(new_sequence) - min(new_sequence) == 4:
                    return [True, 14]
                
            return [False, None]
                
                
        elif len(sequence) == 6:
            if (max(sequence[:5]) - min(sequence[:5]) == 4):
                return [True, sequence[4]]
                
            elif (max(sequence[1:]) - min(sequence[1:]) == 4):
                return [True, sequence[5]]
            
            elif sequence[0] == 1:
                new_sequence = sequence[2:] + [14]
                if max(new_sequence) - min(new_sequence) == 4:
                    return [True, 14]

            return [False, None]
            
        elif len(sequence) == 7:
            if (max(sequence[:5]) - min(sequence[:5]) == 4):
                return [True, sequence[4]]
            
            elif (max(sequence[1:6]) - min(sequence[1:6]) == 4):
                return [True, sequence[5]]
            
            elif (max(sequence[2:]) - min(sequence[2:]) == 4):
                return [True, sequence[6]]
            
            elif sequence[0] == 1:
                new_sequence = sequence[3:] + [14]
                if max(new_sequence) - min(new_sequence) == 4:
                    return [True, 14]

            return [False, None]
            
        
        



if __name__ == '__main__':

    for i in range(100000):
        p1, p2 = random.randint(1,52), random.randint(1,52)
        t1, t2, t3, t4, t5 = random.randint(1,52), random.randint(1,52), random.randint(1,52), random.randint(1,52), random.randint(1,52)

        player = PokerPlayer(p1, p2)
        table = PokerTable(t1, t2, t3, t4, t5)

        

        number_hands = NumberHands(player, table)
        ss_hands = SuiteAndSequenceHands(player, table)

        if ss_hands.valid_game and ss_hands.royal_flush:
            print(p1, p2)
            print(t1, t2, t3, t4, t5)
            print(player.show_cards(), table.show_cards())

            print()
            print(ss_hands.Tell())

            print('-'*50, '\n')
