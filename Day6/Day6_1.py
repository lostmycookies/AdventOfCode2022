# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:19:34 2022

@author: lostmycookies
"""

with open('input.txt') as f:
    inputstring = f.read()

packetmarker = []

for i in range(len(inputstring))[0:(len(inputstring)-3)]:
    char1 = inputstring[i]
    char2 = inputstring[i+1]
    char3 = inputstring[i+2]
    char4 = inputstring[i+3]
    checkset = {char1, char2, char3, char4}
    if len(checkset) == 4:
        packetmarker.append(i+4)
        
print('\nThe start of the package marker is at position: %s' % (packetmarker[0]))
        

