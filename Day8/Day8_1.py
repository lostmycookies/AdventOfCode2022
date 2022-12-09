# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 00:21:48 2022

@author: lostmycookies
"""

with open('input.txt') as f:
    lines = f.read().splitlines()
    
# Data Structures:

treelist = []
treedict = {}
max_x = len(lines[0])-1
max_y = len(lines)-1
    
for i in range(len(lines)):
    for j in range(len(lines[i])):
        treelist.append([i,j])
        treedict[(i,j)] = int(lines[i][j])

def look_around(tree):
    rightBool = True
    leftBool = True
    downBool = True
    upBool = True
    treeX = tree[0]
    treeY = tree[1]
    
    # Corner Check:
        
    if treeX == 0 or treeX == max_x:
        return True
    
    if treeY == 0 or treeY == max_y:
        return True
    
    # Check right
    for i in range(treeY, max_y):
        if treedict[(treeX,treeY)] <= treedict[(treeX,i+1)]:
            rightBool = False
            
    # Check left
    for i in range(0, treeY):
        if treedict[(treeX,treeY)] <= treedict[(treeX,i)]:
            leftBool = False
            
    # Check down
    for i in range(treeX, max_x):
        if treedict[(treeX,treeY)] <= treedict[(i+1,treeY)]:
            downBool = False
    # Check up
    for i in range(0, treeX):
        if treedict[(treeX,treeY)] <= treedict[(i,treeY)]:
            upBool = False
    
    # Visibility-Check:
    
    visible = False
        
    if rightBool or leftBool or downBool or upBool:
        visible = True
        
    return (visible)
    
counter = 0

for tree in treelist:
    if look_around(tree) == True:
        counter += 1
        
print('The number of visible trees ist %s.' % (counter))