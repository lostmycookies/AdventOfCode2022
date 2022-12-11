#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:05:26 2022

@author: lostmycookies
"""

import re

with open('input.txt') as f:
    lines = f.read().splitlines()
    
commands = []

for items in lines:
    commands.append(re.split(" ", items))
    
X = 1
cycle = 0
X_reg_dict = {}

for items in commands:
    if items[0] == 'noop':
        cycle += 1
        X_reg_dict[cycle] = X
    if items[0] == 'addx':
        cycle += 1
        X_reg_dict[cycle] = X
        cycle += 1
        X_reg_dict[cycle] = X
        X += int(items[1])

#################
#   Part 1      #
#################

signal = [20,60,100,140,180,220]
part_1_result = 0

for items in signal:
    part_1_result += items * X_reg_dict[items]
    
    
print('\nThe resulting signal strength is: %s.\n' % (part_1_result))

#################
#   Part 2      #
#################

crt_lines = 6
crt_pixel_per_line = 40
crt = []

for i in range(crt_lines):
    for j in range(1,crt_pixel_per_line+1):
        pos = j-1
        sprite = X_reg_dict[i*crt_pixel_per_line+j]
        sprite = [sprite-1,sprite,sprite+1]
      
        if pos in sprite:
            crt.append('X')
        else:
            crt.append(' ')
    
    print(''.join(crt[i*crt_pixel_per_line:(i+1)*crt_pixel_per_line]))

    



