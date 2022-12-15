# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:38:45 2022

@author: lostmycookies
"""

import math
import re

# Read in the data:
with open('input.txt') as f:
    lines = f.read().splitlines()
   
rocklist = [] 
   
for line in lines:
    rock = [tuple(map(int, xy.split(','))) for xy in line.split(' -> ')]
    rocklist.append(rock)
    
    
def make_rockset(rocklistinput):
    rockset = set()
    bottom = 0
    for walls in rocklist:
        for i in range(len(walls)-1):
            xs = min(walls[i][0],walls[i+1][0])          # xstart
            ys = min(walls[i][1],walls[i+1][1])            
            xe = max(walls[i][0],walls[i+1][0])          # xend
            ye = max(walls[i][1],walls[i+1][1])
            if ye >= bottom:
                bottom = ye
            rockset.add((xs,ys))
            rockset.add((xe,ye))
            if xs == xe:
                for y in range(ys,ye+1):
                    rockset.add((xs,y))
            if ys == ys:
                for x in range(xs,xe+1):
                    rockset.add((x,ys))
    return rockset, bottom
            
# Todo: sand doesn't continue to trickle down

      
def move_sand(rockset, sandsource, void, bottom):
    def drop_sand():
        x = sandsource[0]
        for y in range(bottom):
            for x_move in (0, -1, 1):
                if (x + x_move, y + 1) not in rockset and y + 1 != void:
                    x += x_move
                    break
            else:
                return x , y
    pos = drop_sand()
    while pos and pos != (sandsource):
        rockset.add(pos)
        pos = drop_sand()
    return len(rockset)
    
rockset, bottom = make_rockset(rocklist)
rockref = len(rockset)

# Part 1:

S = (500,0)
bottom = bottom + 1
void = bottom + 2
print('%s units of sand come to rest before sand starts flowing into the abyss below.' % (move_sand(rockset,S,void,bottom)-rockref))

# Part 2:
    
S = (500,0)
bottom = bottom + 1
void = bottom
print('%s units of sand come to rest before sand starts stops flowing.' % (move_sand(rockset,S,void,bottom)-rockref+1)) # 1 extra because the source needs to come to rest as well

