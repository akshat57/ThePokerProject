
# coding: utf-8

# In[49]:


'''
    We divide Hands into two types - NumberHands and SuiteAndSequenceHands
    NumberHands: High Card, Pair, Two Pair, Three of a Kind, Four of a Kind, Full House
    SuiteAndSequenceHands: Straight, Flush, Straight Flush, Royal Flush 

'''


# In[50]:


from Poker import *
from statistics import mode
from operator import itemgetter


# In[51]:


class NumberHands():
    '''
    This class identifies: 
    High Card, Pair, Two Pair, Three of a Kind, Four of a Kind, Full House
    '''
    def __init__(self, Player, Table):
        self.All_Cards(Player, Table)
        self.Frequency()
            
        self.highcard = self.Check_HighCard(Player, Table)
        self.pair = self.Check_Pair(Player, Table)
        self.twopair = self.Check_TwoPair(Player, Table)
        self.threeOfAKind = self.Check_ThreeOfAKind(Player, Table)
        self.fourOfAKind = self.Check_FourOfAKind(Player, Table)
        self.fullHouse = self.Check_FullHouse()
        
    
    def Tell(self):
        print('HighCard = ', self.highcard)
        print('Pair = ', self.pair, '\nTwoPair = ', self.twopair, '\nThree of a Kind = ', self.threeOfAKind , '\nFourofAKinds = ', self.fourOfAKind, '\nFullHouse = ', self.fullHouse  )
  

        

    def All_Cards(self, Player, Table):
        Hand = Player.show_cards() + Table.show_cards()
        self.all_cards = []
        
        for (card, suite) in Hand:
            self.all_cards.append(card)

            
    def Frequency(self):
        self.most_frequent= {}
        
        for card in self.all_cards:
            if card not in self.most_frequent.keys():
                self.most_frequent[card] = 1
            else:
                self.most_frequent[card] += 1
                
        self.most_frequent = dict(sorted(self.most_frequent.items(), key=itemgetter(1), reverse = True))
        self.most_frequent_card = list(self.most_frequent.keys())[0]
        self.next_most_frequent_card = list(self.most_frequent.keys())[1]
        
        if self.most_frequent_card == 1:
            self.high = 14
        else:
            self.high = self.most_frequent_card
            
        if self.next_most_frequent_card == 1:
            self.next_high = 14
        else:
            self.next_high = self.next_most_frequent_card
            
    
    def Check_HighCard(self, Player, Table):
        if min(self.all_cards) == 1:
            return 14
        else:
            return max(self.all_cards)
    
    def Check_Pair(self, Player, Table):
        if self.most_frequent[self.most_frequent_card] >= 2:
            return True
        else:
            return False
        
        
    def Check_TwoPair(self, Player, Table):
        if (self.most_frequent[self.most_frequent_card] >= 2) and (self.most_frequent[self.next_most_frequent_card] >= 2):
            return True
        else:
            return False
        

    def Check_ThreeOfAKind(self, Player, Table):      
        '''To be called after Check_Pair'''
        
        if self.most_frequent[self.most_frequent_card] >= 3:
            return True
        else:
            return False
        
    
    def Check_FourOfAKind(self, Player, Table):
        '''Should be called after Check_Pair and three of a Check_ThreeOfAKind'''

        if self.most_frequent[self.most_frequent_card] == 4:
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
    def __init__(self, Player, Table):
        self.All_Cards(Player, Table)
        
        self.straight = self.Check_Straight(Player, Table)
        self.flush = self.Check_Flush(Player, Table)
        self.straight_flush = self.Check_StraightFlush(Player, Table)
        self.royal_flush = self.Check_RoyalFlush()
        
        
    def Tell(self):
        print('Straight = ', self.straight, '\nFlush = ', self.flush, '\nStraightFlush = ', self.straight_flush, '\nRoyalFlush = ', self.royal_flush)
    
    
    def All_Cards(self, Player, Table):
        Hand = Player.show_cards() + Table.show_cards()
        self.all_cards = []
        
        for (card, suite) in Hand:
            self.all_cards.append(card)
        
    
    def Check_Straight(self, Player, Table):        
        cards = list(set(self.all_cards))
        cards.sort()
        result = self.Check_Sequence_Straight(cards)
        flag = result[0]
        if flag == True:
            self.straight_high = result[1]
        
        return flag
    
    
    def Check_Flush(self, Player, Table):
        suites = Player.all_suites() + Table.all_suites()
        self.most_frequent_suite = max(set(suites), key = suites.count)
    
        if suites.count(self.most_frequent_suite) >= 5:
            Hand = Player.show_cards() + Table.show_cards()
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
        
        
    def Check_StraightFlush(self, Player, Table):##Also Checks for royal Flush
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
            if min(self.sf_cards) == 1 and max(self.sf_cards) == 13:
                return True
            else:
                return False
                
        else:
            return False
        
    
        
    def Check_Sequence_Straight(self, sequence):
        '''
        Input: A sorted list of numbers with NO REPITITION 
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
                else:
                    return [False, None]
            else:
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
                else:
                    return [False, None]
                
            else:
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
                else:
                    return [False, None]
                
            else:
                return [False, None]
            
        
        

