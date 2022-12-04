# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:45:22 2022

@author: lostmycookies
"""


import re

with open('input.txt') as f:
    lines = f.read().splitlines()

counter = 0 
    
for i in range(len(lines)):
    # Get the sections:
    elfpair = re.split('-|,',lines[i])
    elfpair = [int(patch) for patch in elfpair]
    
    set1 = set(range(elfpair[0],elfpair[1]+1))
    set2 = set(range(elfpair[2],elfpair[3]+1))
    
    if set1 & set2:
        counter += 1

print("The final result is %d." % (counter))