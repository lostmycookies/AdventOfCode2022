# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:32:47 2022

@author: lostmycookies
"""

with open('input.txt') as f:
    inputstring = f.read()

packetmarker = []

messagelength = 14

for i in range(len(inputstring))[0:(len(inputstring)-messagelength-1)]:
    checkset = set()
    for j in range(0,messagelength):
        checkset.add(inputstring[i+j])
    if len(checkset) == 14:
        packetmarker.append(i+14)

print('\nThe start of the message marker is at position: %s' % (packetmarker[0]))