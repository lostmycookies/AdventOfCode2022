# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:59:06 2022

@author: polzi
"""


with open('Energy.txt') as f:
    lines = f.read().splitlines()  
 
chonky = 0
counter = 0

for line in lines: 
    if line != "":
        counter += int(line)
    else:
        if counter > chonky:
            chonky = counter
        counter = 0

print(chonky)
