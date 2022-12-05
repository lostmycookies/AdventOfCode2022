# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:33:46 2022

@author: lostmycookies
"""

from collections import deque
import re
import pandas as pd

with open('input.txt') as f:
    lines = f.read().splitlines()
    
# Read in the stacks:

stacklineheader = 8
stackrows = []   

for i in range(stacklineheader):  
    stackrows.append(re.findall('....?',lines[i]))
    
# Transpose and read into a list of deque objects:

df = pd.DataFrame(stackrows).T

stacks = df.values.tolist()

for i in range(len(stacks)):
    tempqueue = deque()
    for j in range(len(stacks[i])):
        if stacks[i][j] != '    ':
            tempqueue.append(stacks[i][j])
    stacks[i] = tempqueue
   
print('\nThe starting stacks(top crate first): \n') 
   
for i in range(len(stacks)):
    print('Stack %s: \n%s\n' %(i+1,list(stacks[i])))

# Read in the moves:
    
stackmovestart = 10

stackmoves = []

for i in range(stackmovestart,len(lines)):
    split = re.split('move | from | to ',lines[i])
    stackmoves.append([int(split[1]),int(split[2])-1,int(split[3])-1]) # Adjusting text columns to data columns

# Go trough the moves:
    
for i in range(len(stackmoves)):
    movenumber = stackmoves[i][0]
    movefrom = stackmoves[i][1]
    moveto = stackmoves[i][2]
    popper = deque()                # Implement another deque object for storage
    for j in range(movenumber):
        popper.append(stacks[movefrom].popleft())
    for j in range(movenumber):
        stacks[moveto].appendleft(popper.pop())

# Output

print('\nThe resulting stacks(top crate first): \n')

for i in range(len(stacks)):
    print('Stack %s: \n%s\n' %(i+1,list(stacks[i])))
    
print('\nThe top crates: \n')

for i in range(len(stacks)):
    print(stacks[i][0])
