# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:40:01 2022

@author: polzi
"""

'''
Opponent Columns

A Rock
B Paper
C Scissors

Your Columns

X Lose
Y Draw
Z Win

Score:
    
1 Rock
2 Paper
3 Scissors

0 Loss
3 Draw
6 Win

'''

with open('input.txt') as f:
    lines = f.read().splitlines()  
    
ruledict = {
    "A X" : 3,
    "A Y" : 4,
    "A Z" : 8,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 2,
    "C Y" : 6,
    "C Z" : 7,
    }

counter = 0

for items in lines:
    counter += ruledict[items]

print("Total number of points is %s" % (counter)) 