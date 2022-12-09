# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:54:51 2022

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

def scenic_score(tree):
    treeX = tree[0]
    treeY = tree[1]
    
    scenic_list  = [0,0,0,0] #right,left,down,up
    
    print('\nTree coordinates: (%s,%s)\n' % (treeX,treeY))
    
    # Look right
    for i in range(treeY, max_y):
        if treedict[(treeX,treeY)] > treedict[(treeX,i+1)]:
            scenic_list[0] += 1
        else:
            scenic_list[0] += 1
            print('    Right view blocked at %s, %s' % (treeX,i+1))
            break
            
    # Look left
    for i in range(treeY-1, -1, -1):
        if treedict[(treeX,treeY)] > treedict[(treeX,i)]:
            scenic_list[1] += 1
        else:
            scenic_list[1] += 1
            print('    Left view blocked at %s, %s' % (treeX,i+1))
            break
            
    # Look down
    for i in range(treeX, max_x):
        if treedict[(treeX,treeY)] > treedict[(i+1,treeY)]:
            scenic_list[2] += 1
        else:
            scenic_list[2] += 1
            print('    Down view blocked at %s, %s' % (treeX,i+1))
            break
        
    # Look up
    for i in range(treeX-1, -1, -1):
        if treedict[(treeX,treeY)] > treedict[(i,treeY)]:
            scenic_list[3] += 1
        else:
            scenic_list[3] += 1
            print('    Up view blocked at %s, %s' % (treeX,i+1))
            break
    
    return scenic_list

# Get the highest score:    

total_score = 0   

scenic_score([4,4])

for items in treelist:
    tempscore = 1
    for entries in scenic_score(items):
        tempscore *= entries
    if tempscore > total_score:
        total_score = tempscore
        best_tree = items
        print('\n    Better tree found at %s with a score of: %s' % (items, total_score))

print('\nHighest possible score is %s at tree %s.' % (total_score,best_tree))


    