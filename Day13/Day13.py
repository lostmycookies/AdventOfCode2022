# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 22:09:44 2022

@author: lostmycookies
"""

import functools
import math

# Read in the data:
with open('input.txt') as f:
    lines = f.read().split('\n\n')

# Generate a pairs datastructure for comparison:
pairs = []
for index, pair in enumerate(lines):
    line = pair.split('\n');
    eval("pairs.append((index, " + line[0] + ", " + line[1] + "))")

# Write a function to compare the pairs:
def compare(pair1: list, pair2: list):
    for a, b in zip(pair1, pair2):
        # Check if both are lists and start recursion if True:
        if isinstance(a, list) and isinstance(b, list):
            result = compare(a, b)
            # Jump out of function if comparison yields result:
            if result == True or result == False:
                return result
        # Check for both integers:
        elif isinstance(a, int) and isinstance(b, int):
            if a < b:
                return True
            elif a > b:
                return False
            else:
                pass 
        # Check of mix of integer and list and recurse if True:
        elif isinstance(a, int) and isinstance(b, list):
            result = compare([a], b)
            if result == True or result == False:
                return result
        elif isinstance(b, int) and isinstance(a, list):
            result = compare(a, [b])
            if result == True or result == False:
                return result
    # Finally, check the length of empty lists if we emptied out from the start
    # or during recursion:
    if len(pair1) > len(pair2):
        return False
    elif len(pair2) > len(pair1):
        return True

#####################
#   Part one:       #
#####################

# Get the list of indices that fulfill the condition:
   
result_index = []

for index, p1, p2 in pairs:
    if compare(p1,p2) == True:
        result_index.append(index+1)

print("\nThe sum of the valid indices is %s" % (sum(result_index)))

#####################
#   Part two:       #
#####################


# Add all the pairs into a long list, put the dividers in:
divider_packets = [[[2]], [[6]]]
sorted_pairs = [[[2]], [[6]]]

for index, p1, p2 in pairs:
    sorted_pairs.append(p1)
    sorted_pairs.append(p2)

# Sort the guy using my sweet sweet sort function popow:
def my_comparison(a,b):
    if compare(a, b) == True:
        return -1
    else:
        return 1

sorted_pairs.sort(key=functools.cmp_to_key(my_comparison))

# Find the positions of the dividers:
divider_index = []

for index, datapack in enumerate(sorted_pairs):
    if datapack in divider_packets:
        divider_index.append(index+1)
                
print("\nThe product of the divider indices is %s" % (math.prod(divider_index)))










