#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:28:47 2022

@author: lostmycookies
"""


import re
import curses
import sys
from statistics import mean 

with open('input.txt') as f:
    lines = f.read().splitlines()

moves = []

for items in lines:
    moves.append(re.split(" ", items))

visit = set()
taillist = []

def direction_change(moveline):
    direction = moveline[0]
    if direction == 'L':
        return [-1,0]
    elif direction == 'R':
        return [1,0]
    elif direction == 'U':
        return [0,1]
    elif direction == 'D':
        return [0,-1]
    
def followup(coordlist):
    tailpos = coordlist[0]
    taillist = []
    for i in range(len(coordlist)):
        headpos = coordlist[i]    
        #check distance to head and move tail:
        dist = [abs(headpos[0]-tailpos[0]),abs(headpos[1]-tailpos[1])]
        if dist[0] > 1 or dist[1] > 1:
           
            # all the moving cases:
            if dist[0] == 2 and dist[1] == 2:
                tailpos = [mean([tailpos[0],headpos[0]]),mean([tailpos[1],headpos[1]])]
                
            if dist[0] == 2 and dist[1] != 2:
                tailpos = [mean([tailpos[0],headpos[0]]),headpos[1]]
                
            if dist[0] != 2 and dist[1] == 2:
                tailpos = [headpos[0],mean([tailpos[1],headpos[1]])]
        taillist.append(tailpos)  
    
    return taillist         
  
mean([1,-1])

def move(moveinput):
    movelist = moveinput
    headpos = [0,0]
    tailpos = [0,0]
    
    for items in movelist:

        for i in range(0,int(items[1])):
            # move the head
            move_vector = direction_change(items)
            headpos[0] = headpos[0] + move_vector[0]
            headpos[1] = headpos[1] + move_vector[1]
        
            #check distance to head and move tail:
            dist = [abs(headpos[0]-tailpos[0]),abs(headpos[1]-tailpos[1])]
            if dist[0] > 1 or dist[1] > 1:
               
                # diagonal follow:
                if headpos[0] != tailpos[0] and headpos[1] != tailpos[1]:
                    
                    if dist[0] == 2:
                        tailpos = [mean([tailpos[0],headpos[0]]),headpos[1]]

                    if dist[1] == 2:
                        tailpos = [headpos[0],mean([tailpos[1],headpos[1]])]
                            
                # x-axis follow:
                elif dist[1] <= 1:
                    tailpos = [mean([tailpos[0],headpos[0]]),tailpos[1]]
                    
                # y-axis follow:
                elif dist[0] <= 1:
                    tailpos = [tailpos[0], mean([tailpos[1],headpos[1]])]                  
            
            taillist.append(tailpos)
            visit.add(str(tailpos))
    return taillist

  
##################
# Part 1:        #
##################  
  
tail_2 = move(moves)

print('The tail visited %s spaces.' % (len(visit)))


##################
# Part 2:        #
##################


tailknots = 9

def snakey(coordlist,ropelength):
    inlist = coordlist
    outlist = []
    for i in range(ropelength-1):
        outlist.append(followup(inlist))
        inlist = outlist[-1]
    return outlist

result = snakey(tail_2,9)

resultset = set()

for i in range(len(result[-1])):
    resultset.add(str(result[-1][i]))
    
print('The visited spaces for a %s-segment long rope are %s in total.' % (tailknots+1,len(resultset)))
