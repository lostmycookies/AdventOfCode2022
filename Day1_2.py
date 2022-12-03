# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:23:07 2022

@author: polzi
"""


with open('Energy.txt') as f:
    lines = f.read().splitlines()  
 
counter = 0

lechonk = []

for line in lines: 
    if line != "":
        counter += int(line)
    else:
        lechonk.append(counter)
        counter = 0

lechonk.sort(reverse=True)

print(sum(lechonk[0:3]))