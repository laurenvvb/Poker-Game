#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:47:22 2018

marking ID: 5675
"""

import copy
from Card import Card, Hand, Deck

class ThreeCardPokerDeck(Deck):
    """
    Three-Card Poker deck
    """
    
    def deal_hand(self, name=""):
        """
        Creates a new instance of ThreeCardPokerHand
        hand and initializes it with 3 cards from the deck.
        An optional name argument can be used to specify the 
        name of the player.
        Returns the instance of ThreeCardPokerHand thus created
        """
        hand = ThreeCardPokerHand(self.pop_cards(3), name)
        return hand

class ThreeCardPokerHand(Hand):
    """
    Three-Card Poker hand
    """
    
    all_labels = ['Nothing', 'Pair', 'Flush', 'Straight', 'Three of a Kind',
                  'Straight Flush']
    
#   Question 2
    def _compute_rank(self):
        """
        self, this instance of ThreeCardPokerHand
        Computes the ranking of self and stores it 
        in the self.rank attribute according to the 
        rules described in Question 2 of the project brief.
        Returns None
        """
        Card.ranks[9] = '11' #jack
        Card.ranks[10] = '12' #queen
        Card.ranks[11] = '13' #king
        Card.ranks[12] = '14' #ace
    
        # Straight Flush
        if len(set(self.suits)) == 1 and (int(self.ranks[0]) - int(self.ranks[2]) == 2 or int(self.ranks[0]) - int(self.ranks[2]) == 12):
            self.rank = 5
        # Three of a kind
        elif len(set(self.ranks)) == 1:
            self.rank = 4
        # Straight
        elif int(self.ranks[0]) - int(self.ranks[2]) == 2 or int(self.ranks[0]) - int(self.ranks[2]) == 12:
            self.rank = 3
        # Flush
        elif len(set(self.suits)) == 1 and int(self.ranks[0]) - int(self.ranks[2]) != 2:
                self.rank = 2
        # Pair
        elif self.ranks[0] == self.ranks[1] and self.ranks[0] != self.ranks[2]:
            self.rank = 1
        elif self.ranks[0] == self.ranks[2] and self.ranks[0] != self.ranks[1]:
            self.rank = 1
        elif self.ranks[1] == self.ranks[2] and self.ranks[0] != self.ranks[2]:
            self.rank = 1
        # Else
        else:
            self.rank = 0
        
        # convert the cards back 
        Card.ranks[9] = 'Jack'
        Card.ranks[10] = 'Queen' 
        Card.ranks[11] = 'King' 
        Card.ranks[12] = 'Ace' 
        

#   Question 3    
    def _compare(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Implements the comparison rules for two ThreeCardPoker
        hands as per the description in Question 3 of the project brief.
        Returns -1 if other is a winning hand, 1 if self is the winning hand,
        and 0 if self and other are tied up.
        """
        Card.ranks[9] = '11' #jack
        Card.ranks[10] = '12' #queen
        Card.ranks[11] = '13' #king
        Card.ranks[12] = '14' #ace
        if self.rank > other.rank:
            return 1
        elif other.rank > self.rank:
            return -1
        elif self.rank == other.rank:
            # straight or straight flush
            if self.rank == 5:
                Card.ranks[12] = '1'
                if max(self.ranks) > max(other.ranks):
                    return 1
                elif max(other.ranks) > max(self.ranks):
                    return -1
                else:
                    return 0
            elif self.rank == 3:
                Card.ranks[12] = '1'
                if max(self.ranks) > max(other.ranks):
                    return 1
                elif max(other.ranks) > max(self.ranks):
                    return -1
                else:
                    return 0
            # 3 of a kind
            elif self.rank == 4:
                if self.ranks[0] > other.ranks[0]:
                    return 1
                elif other.ranks[0] > self.ranks[0]:
                    return -1
                else:
                    return 0 
            # flush or nothing
            elif self.rank == 2 or self.rank == 0:
                if self.ranks[0] > other.ranks[0]:
                    return 1
                elif other.ranks[0] > self.ranks[0]:
                    return -1
                elif self.ranks[0] == other.ranks[0]:
                    if self.ranks[1] > other.ranks[1]:
                        return 1
                    elif other.ranks[1] > self.ranks[1]:
                        return -1
                    elif self.ranks[1] == other.ranks[1]:
                        if self.ranks[2] > other.ranks[2]:
                            return 1
                        elif other.ranks[2] > self.ranks[2]:
                            return -1
                        elif self.ranks[2] == other.ranks[2]:
                            return 0
            # pairs
            elif self.rank == 1:
                if self.ranks[0]==self.ranks[1]>other.ranks[0]==other.ranks[1] or self.ranks[0]==self.ranks[2]>other.ranks[0]==other.ranks[1] or self.rank[1]==self.rank[2]>other.ranks[0]==other.ranks[1]:
                    return 1
                elif self.ranks[0]==self.ranks[1]<other.ranks[0]==other.ranks[1] or self.ranks[0]==self.ranks[2]<other.ranks[0]==other.ranks[1] or self.rank[1]==self.rank[2]<other.ranks[0]==other.ranks[1]:
                    return -1
                elif self.ranks[0]==self.ranks[1]==other.ranks[0]==other.ranks[1]:
                    if self.ranks[2]>other.ranks[2]:
                        return 1
                    elif other.ranks[2]>self.ranks[2]:
                        return -1
                    else:
                        return 0
                elif self.ranks[0]==self.ranks[2]==other.ranks[0]==other.ranks[1]:
                    if self.ranks[1]>other.ranks[2]:
                        return 1
                    if other.ranks[2]>self.ranks[1]:
                        return -1
                    else:
                        return 0
                elif self.ranks[1]==self.ranks[2]==other.ranks[0]==other.ranks[1]:
                    if self.ranks[0]>other.ranks[2]:
                        return 1
                    elif other.ranks[2]>self.ranks[0]:
                        return -1
                    else:
                        return 0
                
                elif self.ranks[0]==self.ranks[1]>other.ranks[0]==other.ranks[2] or self.ranks[0]==self.ranks[2]>other.ranks[0]==other.ranks[2] or self.rank[1]==self.rank[2]>other.ranks[0]==other.ranks[2]:
                    return 1
                elif self.ranks[0]==self.ranks[1]<other.ranks[0]==other.ranks[2] or self.ranks[0]==self.ranks[2]<other.ranks[0]==other.ranks[2] or self.rank[1]==self.rank[2]<other.ranks[0]==other.ranks[2]:
                    return -1
                elif self.ranks[0]==self.ranks[1]==other.ranks[0]==other.ranks[2]:
                    if self.ranks[2]>other.ranks[1]:
                        return 1
                    elif other.ranks[2]>self.ranks[1]:
                        return -1
                    else:
                        return 0
                elif self.ranks[0]==self.ranks[2]==other.ranks[0]==other.ranks[2]:
                    if self.ranks[1]>other.ranks[1]:
                        return 1
                    if other.ranks[1]>self.ranks[1]:
                        return -1
                    else:
                        return 0
                elif self.ranks[1]==self.ranks[2]==other.ranks[0]==other.ranks[2]:
                    if self.ranks[0]>other.ranks[1]:
                        return 1
                    elif other.ranks[1]>self.ranks[0]:
                        return -1
                    else:
                        return 0
                    
                elif self.ranks[0]==self.ranks[1]>other.ranks[1]==other.ranks[2] or self.ranks[0]==self.ranks[2]>other.ranks[1]==other.ranks[2] or self.rank[1]==self.rank[2]>other.ranks[1]==other.ranks[2]:
                    return 1
                elif self.ranks[0]==self.ranks[1]<other.ranks[1]==other.ranks[2] or self.ranks[0]==self.ranks[2]<other.ranks[1]==other.ranks[2] or self.rank[1]==self.rank[2]<other.ranks[1]==other.ranks[2]:
                    return -1
                elif self.ranks[0]==self.ranks[1]==other.ranks[1]==other.ranks[2]:
                    if self.ranks[2]>other.ranks[0]:
                        return 1
                    elif other.ranks[0]>self.ranks[2]:
                        return -1
                    else:
                        return 0
                elif self.ranks[0]==self.ranks[2]==other.ranks[1]==other.ranks[2]:
                    if self.ranks[1]>other.ranks[0]:
                        return 1
                    if other.ranks[0]>self.ranks[1]:
                        return -1
                    else:
                        return 0
                elif self.ranks[1]==self.ranks[2]==other.ranks[1]==other.ranks[2]:
                    if self.ranks[0]>other.ranks[0]:
                        return 1
                    elif other.ranks[0]>self.ranks[0]:
                        return -1
                    else:
                        return 0
            # else
            else:
                return 0
    
    def get_rank(self):
        """
        getter method for the 
        rank attribute
        Returns 0, 1, 2, 3, 4, 5 if the
        self's rank is respectively Nothing, 
        Pair, Flush, Straight, Three of a Kind, and Straight Flush
        """
        return self.rank

    def __init__(self, cards, name=""):
        Hand.__init__(self, name)
        self.cards = copy.deepcopy(cards)
        self.ranks = [card.get_rank() for card in self.cards]
        self.ranks.sort(reverse = True)
        self.suits = [card.get_suit() for card in self.cards]
        self._compute_rank()

    def __lt__(self, other):
        return True if self._compare(other) < 0 else False
    
    def __le__(self, other):
        return True if self._compare(other) <= 0 else False

#   Question 3
    def __gt__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self is the winning hand, False otherwise
        """
        # greater than
        return True if self._compare(other) > 0 else False
    
#   Question 3    
    def __ge__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self is the winning hand or
        self and other are tied; False otherwise
        """
        # greather than or equal
        return True if self._compare(other) >= 0 else False
    
#   Question 3    
    def __eq__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self and other are tied; 
        False otherwise
        """
        # equal
        return True if self._compare(other) == 0 else False

#   Question 3    
    def __ne__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self and other are not tied; 
        False otherwise
        """
        # not equal
        return True if self._compare(other) != 0 else False

    def get_label(self):
        """
        self, this instance of ThreeCardPokerHand
        Returns a string representation of self.
        """
        return ThreeCardPokerHand.all_labels[self.rank]
    
    def get_full_label(self):
        """
        self, this instance of ThreeCardPokerHand
        Returns a string representation of self replacing
        the Nothing ranking with the highest ranking card.
        Used internally by __str__().
        """
        return  Card.ranks[self.ranks[0]] + '-High' if self.rank == 0 else \
            self.get_label()
        
    def __str__(self):
        """
        self, this instance of ThreeCardPokerHand
        Returns a string representation of self that 
        includes the list of the cards, and the rank.
        """
        return Hand.__str__(self) + '\nHand Rank: ' + self.get_full_label()
        
          
if __name__ == '__main__':
    """
    Test cases
    """
#   Queen-high
    hand1 = ThreeCardPokerHand([Card(10, 0), Card(1, 1), Card(0, 2)])
    print(hand1)
    print()

#   Straight Flush
    hand2 = ThreeCardPokerHand([Card(12, 0), Card(1, 0), Card(0, 0)])
    print(hand2)
    print()
    
    print(hand1 < hand2) # True
    print(hand1 > hand2) # False
    print(hand1 <= hand2) # True
    print(hand1 >= hand2) # False
    print(hand1 == hand2) # False
    print(hand1 != hand2) # True
    print()
    
#   3-Pair + Jack
    hand1 = ThreeCardPokerHand([Card(1, 0), Card(1, 1), Card(9, 2)])
    print(hand1)
    print()

#   2-Pair + Ace
    hand2 = ThreeCardPokerHand([Card(12, 0), Card(0, 1), Card(0, 0)])
    print(hand2)
    print()
    
    print(hand1 < hand2) # False
    print(hand1 > hand2) # True
    print(hand1 <= hand2) # False
    print(hand1 >= hand2) # True
    print(hand1 == hand2) # False
    print(hand1 != hand2) # True
    print()


    deck = ThreeCardPokerDeck()
    deck.shuffle()
    hand = deck.deal_hand()
    print(hand)

#   Straight Flush    
    print()
    hand3 = ThreeCardPokerHand([Card(0, 0), Card(1, 0), Card(12, 0)], 'Ruben')
    print(hand3)

#   Straight    
    print()
    hand3 = ThreeCardPokerHand([Card(0, 1), Card(12, 2), Card(1, 0)], 'Greg')
    print(hand3)  

#   Straight Flush    
    print()
    hand3 = ThreeCardPokerHand([Card(12, 1), Card(10, 1), Card(11, 1)], 'Dealer')   
    print(hand3)                      
    
#   Flush
    print()
    hand3 = ThreeCardPokerHand([Card(0, 1), Card(1, 1), Card(11, 1)], 'Player')   
    print(hand3)                      