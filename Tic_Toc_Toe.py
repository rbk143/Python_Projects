# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:35:55 2020

@author: bbharathkumar
"""
import random

def print_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player():
    a = random.randint(0, 1)
    if a == 0:
        return "Player 1"
    elif a == 1:
        return "player 2"

def marker(player):
    b = "wrong"
    while b not in ['X','O']:
        b = input(player +" : Please enter your marker (X or O) : ")
        if b not in ['X','O']:
            print("Please enter 'X' or 'O'")
    return b

"Game Starts now"

def position(board):
    c = 0
    while (board[c] != ' ')or( board[c] in ['X','O'] )and c not in range(1,10):
        c = int(input("Enter the position to place your marker :"))
    return c

def mark_it(position,board,marker):
    board[position] = marker
    if marker == 'X':
        marker = 'O'
    elif marker == 'O':
        marker = 'X'
    return marker
    
def logic(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def main():
    TT = ["#"," "," "," "," "," "," "," "," "," ",]
    mark = marker(player())
    marknxt = mark
    while logic(TT,mark)==False:
        mark = marknxt
        p = position(TT)
        marknxt = mark_it(p, TT, mark)
        print_board(TT)
    print("Congratulation you have won the game")
    
main()