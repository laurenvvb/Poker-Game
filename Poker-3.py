#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:25:20 2018

marking ID: 5675
"""

from PokerHand import ThreeCardPokerDeck, ThreeCardPokerHand
from Card import Card

# Question 4
def make_dist(n):
    """
    n, a positive integer
    Runs n trials of comprising of dealing 
    a Three-Card Poker hand from a randomly shuffled
    deck, and summarizing the percentage probabilities 
    of the possible hand ranks represented as strings.
    Returns a dictionary mapping the hand tring labels to 
    float percentages.
    """
    Straight_Flush = 0
    Nothing = 0
    Pair = 0
    Flush = 0
    Straight = 0
    Three_of_a_kind = 0
    for i in range(n):
        deck = ThreeCardPokerDeck()
        deck.shuffle()
        hand = deck.deal_hand()
        if hand.get_label() == 'Straight Flush':
            Straight_Flush = Straight_Flush +1
        elif hand.get_label() == 'Nothing':
            Nothing = Nothing +1
        elif hand.get_label() == 'Pair':
            Pair = Pair+1
        elif hand.get_label() == 'Flush':
            Flush = Flush +1
        elif hand.get_label() == 'Straight':
            Straight = Straight+1
        elif hand.get_label() == 'Three of a Kind':
            Three_of_a_kind = Three_of_a_kind+1
    p = Pair/n
    no = Nothing/n
    f = Flush/n
    s = Straight/n
    sf = Straight_Flush/n
    t = Three_of_a_kind/n
    print("{'Pair':%.2f, 'Nothing':%.2f, 'Flush':%.2f, 'Straight':%.2f, 'Straight Flush':%.2f, 'Three of a Kind':%.2f}" %(p*100, no*100, f*100, s*100, sf*100, t*100))

# A ThreeCardPokerHand object initialized with the 
# smallest hand that can be played by the dealer. 
# Use it to determine if the dealer's hand can play
# in your play_round code 
min_dealer_hand = ThreeCardPokerHand([Card(10, 0), Card(1, 1), Card(0, 2)])

# Question 5
def play_round(dealer_hand, player_hand, cash, get_ante, is_playing):
    """
    dealer_hand, an instance of ThreeCardPokerHand holding the
    hand dealt to the dealer at the beginning of the round
    player_hand, an instance of ThreeCardPokerHand holding the
    hand dealt to the dealer at the beginning of the round
    cash, a positive integer, the amount of cash available to the 
    player at the beginning of the round
    get_ante, a function, takes cash as argument and returns 
    the player's ante bet
    is_playing, a function, takes the player's hand as arugment
    and returns True if the player plays, and False if the player folds.
    Returns: tuple (ante, outcome), ante is the ante bet
    returned by get_ante, and outcome is  
    -2 if the dealer qualifies, the player plays and loses,
    -1 if the player folds
    0 if the dealer qualifies, the player plays, and the hands tie up
    1 if the dealer does not qualify, and the player plays.
    """
    cash = get_ante(cash)
    player_hand1 = is_playing(player_hand)
    if player_hand1 == False:
        return (cash, -1)
    elif player_hand1 == True:
        if dealer_hand < min_dealer_hand:
            return (cash, 1)
        else:
            if player_hand > dealer_hand:
                return (cash, 2)
            else:
                return (cash, -2)
    
def get_ante(cash):
    """
    A sample get_ante function.
    Feel free to customize as needed
    """
    return int(input('Enter your ante bet (Cash=' + str(cash) + '): '))
    
def is_playing(player_hand):
    """
    A sample is_playing function.
    Feel free to customize as needed.
    """
    print(player_hand)
    return True if input("Play or fold  (p/f): ") == 'p' else False

def proc_outcome(outcome, ante, dealer_hand):
    """
    A sample function to process the outcome
    of the round. 
    Feel free to customize as needed.
    """
    out = ['Tie', 'Dealer does not qualify', 'You won', 'You lost', 'You folded']
    payoff = outcome * ante
    print(dealer_hand)
    print(out[outcome] + ': ' + ('+' if payoff > 0 else '') + str(payoff))
    return payoff

def play(trials, stake, goal):
    """
    trials, positive integer, the number of trial game runs
    stake, positive integer, the initial amount of cash available to the player
    goal, the amount of cash the player is hoping to have by the end of each trial game
    Runs the trials number of trial games of Three-Hand Poker. Each trial run
    proceeds as long as the amount of cash available to the player is 
    both positive and below the goal. Each round is implemented by 
    calling the play_round() function below. 
    Prints various stats upon termination.
    """
    wins, gain, rounds, win_rounds, tie_rounds, lose_rounds = 0, 0, 0, 0, 0, 0
    for _ in range(trials):
        cash = stake
        while cash > 0 and cash < goal:
            deck = ThreeCardPokerDeck()
            deck.shuffle()
            player_hand = deck.deal_hand("Player")
            dealer_hand = deck.deal_hand("Dealer")
#           Invoke your implementation of play_round
            (ante, outcome) = \
                play_round(dealer_hand, player_hand, cash, get_ante, is_playing)
            cash += proc_outcome(outcome, ante, dealer_hand)
            rounds += 1
            win_rounds += 1 if outcome > 0 else 0
            tie_rounds += 1 if outcome == 0 else 0
            lose_rounds += 1 if outcome < 0 else 0
        wins += 1 if cash >= goal else 0
        gain += cash - stake
    print('Finished', trials, 'trial games')
    print('Winning games (%)', 100 * wins / trials)
    print('Average gain per game', gain / trials)
    print('Average number of rounds per game:', rounds / trials)
    print('Average number of winning rounds per game:', win_rounds / trials)
    print('Average number of tied rounds per game:', tie_rounds / trials)
    print('Average number of losing rounds per game:', lose_rounds / trials)

if __name__ == '__main__':
#   Estimate Three-Card Poker hand probabilities by running 
#   10000 random hand deals
    print(make_dist(10000))
    
#   This will play a single game of Three-Card Poker with the
#   initial stake of 100, and a goal to turn it into 200.
    play(1, 100, 200)
 