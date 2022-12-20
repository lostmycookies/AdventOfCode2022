# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:34:26 2022

@author: lostmycookies
"""


import math
import re

# Read in the data:
with open('input.txt') as f:
    lines = f.read().splitlines()

# Get the data structure: 
sensorlist = []
sensors = set()
beacons = set()

for items in lines:
    sx,sy,bx,by = re.findall('[+-]?\d+', items)
    sx,sy,bx,by = int(sx),int(sy),int(bx),int(by)
    sensorlist.append((sx,sy,bx,by))
    distance = abs(sx-bx) + abs(sy-by) # Get the manhattan distance to the closest beacon
    sensors.add((sx,sy,distance))
    beacons.add((bx,by))
    

def can_contain(x,y):
    for sx,sy,distance in sensors:
        if distance >= abs(x-sx) + abs(y-sy) and (x,y) not in beacons:
            return False
    return True
        
def row_checker(y):
    counter = 0
    for x in range(min(x-distance for x,_,distance in sensors), max(x+distance for x,_,distance in sensors)):
        if not can_contain(x,y) and (x,y) not in beacons:
            counter += 1
    return counter
    

def tuning_frequency(inputrange): # Function to reduce the number of spots to check by only checking the points that extend concentrical around the beacons
    for sx, sy, d in sensors:
        for dx in range(d + 2): # Check horizontal until 1 outside the maximum manhattan distance
            dy = (d + 1) - dx # Get the vertical position based on the horizontal alignment
            for horizontal, vertical in [(1,1),(1,-1),(-1,1),(-1,-1)]: 
                x, y = sx + (dx * horizontal), sy + (dy * vertical)
                if not(0 <= x <= inputrange and 0<=y<=inputrange): # Only allow input combinations within the input range
                    continue
                if can_contain(x, y): # If within allowable range, check if the spot is free from beacon reach
                    return x * 4000000 + y

# Part 1:

cave_row = 2000000    

print('There are %s positions where a beacon cannot be present.' % (row_checker(cave_row)))

# Part 2:
    
inputrange = 4000000
    
print('The tuning frequency is: %s.' % (tuning_frequency(inputrange)))