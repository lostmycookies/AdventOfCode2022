# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:06:24 2022

@author: polzi
"""

'''
Opponent Columns

A Rock
B Paper
C Scissors

Your Columns

X Rock
Y Paper
Z Scissors

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
    "C X" : 6,
    "A Y" : 6,
    "B Z" : 6,
    "A X" : 3,
    "B Y" : 3,
    "C Z" : 3,
    "B X" : 0,
    "C Y" : 0,
    "A Z" : 0,
    "X" : 1,
    "Y" : 2,
    "Z" : 3
    }


counter = 0

for items in lines:
    counter += ruledict[items]
    counter += ruledict[items[2]]

print("Total number of points is %s" % (counter)) 
    
