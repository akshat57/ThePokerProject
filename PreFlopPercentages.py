
# coding: utf-8

# In[3]:


'''
    Here we start a poker game
'''


# In[1]:


from PokerHands import *
from PokerRules import *
import random


# In[2]:


class Game(Check_Hand):
    def __init__(self, heros_hand, num_players, seed):
        self.taken_card = [heros_hand[0], heros_hand[1]]
        self.num_players = num_players
    
        self.Hero = PokerPlayer(heros_hand[0], heros_hand[1])
        self.Other_Players()
        self.Table = PokerTable( self.new_card(), self.new_card(), self.new_card(), self.new_card(), self.new_card())
        self.Play_Game()
        
        
    def Other_Players(self):
        self.Players = []
        for i in range(self.num_players-1):
            self.Players.append(PokerPlayer( self.new_card(), self.new_card()))
                
    def new_card(self):
        for t in range(50):
            card = random.randint(1,52)
            if card not in self.taken_card:
                self.taken_card.append(card)
                break
        
        return card
    
    
    def Play_Game(self):
        self.player_results = []
        
        hero_hand = Check_Hand(self.Hero, self.Table)
        self.player_results.append([hero_hand.points, hero_hand.high, hero_hand.next_high, PointsToHand(hero_hand.points)])
        
        for i in range(self.num_players-1):
            player_hand = Check_Hand(self.Players[i], self.Table)
            self.player_results.append([player_hand.points, player_hand.high, player_hand.next_high, PointsToHand(player_hand.points) ])
                      
        self.Winner()
        if self.winner == 0:
            self.heroWins = True
            self.split = False
            self.heroLost = False
        elif self.winner == -1:
            self.heroWins = False
            self.split = True
            self.heroLost = False
        else:
            self.heroWins = False
            self.split = False
            self.heroLost = True
            
        #self.Show_Game()
        
    
    
    def Winner(self):
        winner = 0
        
        for i in range(1,self.num_players):
            if self.player_results[i][0] > self.player_results[winner][0]:
                winner = i
                
            elif self.player_results[i][0] == self.player_results[winner][0]:
                if (self.player_results[i][2] != None and self.player_results[winner][2] != None):
                    if self.player_results[i][1] > self.player_results[winner][1]:
                        winner = i
                    
                    elif self.player_results[i][1] == self.player_results[winner][1]:
                        if (self.player_results[i][2] != None and self.player_results[winner][2] != None):
                            if self.player_results[i][2] > self.player_results[winner][2]:
                                winner = i
                        else:
                            winner = -1
                else:
                    winner = -1
               
        self.winner = winner
        return True

    
    def Show_Game(self):
        print('############TABLE##########')
        print(self.Table.show_cards())
        print('############TABLE###########')
        print('')
        
        if self.winner == 0:
            print('WINNER = HERO!!')
            print(self.Hero.show_cards(), self.player_results[self.winner][3])
            print('\nOther Players')
            
            for i in range(self.num_players-1):
                print(self.Players[i].show_cards(), self.player_results[i+1][3])
            
        elif self.winner == -1:
            print('SPLIT POT')
            print('\nAll Players')
            print(self.Hero.show_cards())
            for i in range(self.num_players-1):
                print(self.Players[i].show_cards(), self.player_results[i+1][3])
        else:
            print('WINNER = PLAYER ', self.winner)
            print(self.Players[self.winner-1].show_cards())
            
            print('\nOther Players')
            print(self.Hero.show_cards())
            for i in range(self.num_players-1):
                if i != self.winner-1:
                    print(self.Players[i].show_cards(), self.player_results[i+1][3])
            
                  


# In[89]:


class MyHand_Odds(Game):
    '''
    num_players = number of players in the game
    Card1 = First Card, as a string
    Card2 = Second Card, as a string
    Suite = This can be 'Suited' or 'OffSuited'
    N = number of test hands
    '''
    def __init__(self, num_players, Card1, Card2, Suite, N = 10000):
        self.C1 = Card1
        self.C2 = Card2
        self.num_players = num_players
        self.Suite = Suite
        self.N = N
        
        self.get_odds()
        
        
        
    def get_odds(self):
        if self.Suite == 'Suited':
            hero = [self.C1, self.C2]
        else:
            hero = [self.C1, 13 + self.C2]
            
        hero_wins = 0
        split = 0
        hero_lost = 0
        
        for i in range(self.N):
            
            result = Game(hero, self.num_players, i)
    
            if result.heroWins:
                hero_wins += 1
            elif result.split:
                split += 1
            elif result.heroLost:
                hero_lost += 1
        
        self.win = hero_wins/N
        self.split = split/N
        self.lost = hero_lost/N
        
            
        
            
        
        
        


# In[ ]:


####Best Off- Suited Hands
num_players = 8

f= open( str(num_players) + "players.txt","w")

suite = 'OffSuited'
sequence = [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

counter = 0
total = 0
for i, card1 in enumerate(sequence):
    for j in range(i, 13):
        total += 1
        card2 = sequence[j]
        MyHand = MyHand_Odds(num_players, card1, card2, suite).win 
        if MyHand > 1/num_players:
            #print(card1, card2, suite,  MyHand)
            f.write("%d %d %s %f \n" %(card1, card2, suite,  MyHand))
            counter += 1
            
num_offsuited = counter
total_offsuited = total
f.write("\n Percentage of off-suited hands you I should play = %f" %(counter/float(total)))
#print('\n Percentage of off-suited hands you I should play = ', counter/total)
print('\n')
f.write('\n')

suite = 'Suited'
sequence = [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

for i, card1 in enumerate(sequence):
    for j in range(i+1, 13):
        total += 1
        card2 = sequence[j]
        MyHand = MyHand_Odds(num_players, card1, card2, suite).win 
        if MyHand > 1/num_players:
            #print(card1, card2, suite,  MyHand)
            f.write("%d %d %s %f \n" %(card1, card2, suite,  MyHand))
            counter += 1
            
f.write("\n Percentage of suited hands you I should play = %f" %((counter-num_offsuited)/float(total-total_offsuited)))
f.write('\n')
#print('\n Percentage of suited hands you I should play = ', (counter-num_offsuited)/(total-total_offsuited))
#print('\n')

#print('Percentage of hands you should play = ', counter / total)
f.write('Percentage of hands you should play = %f' %(counter / float(total)))
f.close()

