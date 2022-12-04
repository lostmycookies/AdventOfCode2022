# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:45:21 2022

@author: lostmycookies
"""

import re

with open('input.txt') as f:
    lines = f.read().splitlines()


##############################################
# First try                                  #
##############################################  
    

counter = 0 

    
for i in range(len(lines)):
    # Get the sections:
    elfpair = re.split('-|,',lines[i])
    elfpair = [int(patch) for patch in elfpair]
    elfrange1 = len(range(elfpair[0],elfpair[1]))
    elfrange2 = len(range(elfpair[2],elfpair[3]))
    marker = elfrange1 - elfrange2
    
    # Go through the cases:
    if (marker == 0) & (elfpair[0] == elfpair[2]) & (elfpair[1] == elfpair[3]):
        counter += 1
        
    elif (marker > 0) & (elfpair[2] >= elfpair[0]) & (elfpair[1] >= elfpair[3]):
        counter += 1
        
    elif (marker < 0) & (elfpair[0] >= elfpair[2]) & (elfpair[3] >= elfpair[1]):
        counter += 1

print("The final result is %d." % (counter))

##############################################
# Second attempt after doing the other part: #
##############################################    


counter = 0

    
for i in range(len(lines)):
    # Get the sections:
    elfpair = re.split('-|,',lines[i])
    elfpair = [int(patch) for patch in elfpair]
    
    set1 = set(range(elfpair[0],elfpair[1]+1))
    set2 = set(range(elfpair[2],elfpair[3]+1))

    #print(set1.issubset(set2))
    if set1 != set2:
        if (set1.issubset(set2)):
            counter += 1
            
        if (set2.issubset(set1)):
            counter += 1
    else:
        counter += 1
           
print("The final result with the alternative approach is %d." % (counter))