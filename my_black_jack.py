# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 08:47:52 2020

@author: bbharathkumar
"""


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
win_bool = True
deck = []

for suit in suits:
    for rank in ranks:
        deck.append((suit,rank))

def shuffle(deck):
    random.shuffle(deck)

class Card():
    
    def __init__(self,x):
        self.x = x
        self.cards = []
        self.aces = 0
        self.sum = 0
        
    def adder(self,popped):
        suit,rank = popped
        self.sum += values[rank]
        self.cards.append(popped)
        if rank == 'Ace':
            self.aces += 1
        
    def checker(self):
        while self.sum > 21 and self.aces != 0:
            self.sum -= 10
            self.aces -= 1
            
        return self.sum
            
        
    def show(self):
        print('\n---' + self.x +" has these cards---")
        for x,y in self.cards:
            print(x+' of '+y)
    
    def bot_show(self):
        print('\n---' +self.x +" has these cards---")
        print("<<<This card is hidden>>>")
        x,y = self.cards[1]
        print( x+' of '+y)
        
def serve(deck):
    popped = ()
    popped = deck.pop()
    return popped

while playing:
    shuffle(deck)
    bot = Card('bot')
    player = Card('player')
    for z in range(2):
        bot.adder(serve(deck))
        player.adder(serve(deck))
    bot.bot_show()
    player.show()
    
    while win_bool:
        hit = input("Do you wish to hit or stay(H or S) :")
        if hit == 'H':
            bot.adder(serve(deck))
            player.adder(serve(deck))
            bot.bot_show()
            player.show()
            check = player.checker()
            bot_check = bot.checker()
            if check > 21:
                win_bool = False
                print("\n***Bot wins!!***")
        if hit == 'S':
            print("!@#$%^&*)(Bot is revealing)(*&^%$#@!")
            bot.show()
            player.show()
            check = player.checker()
            bot_check = bot.checker()
            if bot_check > 21:
                print("\n***Player wins!!***")
                break
            elif bot_check > check:
                print('\n***Bot wins!!***')
            elif bot_check == check:
                print("\n***It's a tie***")
            else:
                print("\n***Player wins!!***")
            win_bool = False
    print(("\nbot total value is :{}").format(bot_check))
    print(("Player total value is :{}").format(check))
    
    yn = input("Do you wish to give it another try(Y or N) : ")
    if yn=='Y':
        win_bool = True
    else:
        playing = False
        print("\n$THE END$")