# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 21:06:00 2022

@author: lostmycookies
"""


import re
import string
from collections import deque

##################
#   Functions    #
##################

def make_nodes (lines):
    node_list = [] 
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            node_list.append((i,j))
            if lines[i][j] == 'S':
                S = (i,j)
            if lines[i][j] == 'E':
                E = (i,j)
                
    return node_list,S,E

def find_letter(input):
    letterpos = []
    for i in range(len(lines)):
        for j in range(len(lines[i])): 
            if lines[i][j] == input:
                 letterpos.append((i,j))
    return letterpos
                 
def make_arcs (lines,val_dict):
    arclist = []
    # horizontal neighbours
    for i in range(len(lines)):
        for j in range(len(lines[i])-1):
            x_adjacent_right = lines[i][j],lines[i][j+1]
            x_adjacent_left = lines[i][j+1],lines[i][j]
            if check_climb(x_adjacent_right[0], x_adjacent_right[1],val_dict) == True:
                arclist.append(((i,j),(i,j+1)))
            if check_climb(x_adjacent_left[0], x_adjacent_left[1],val_dict) == True:
                arclist.append(((i,j+1),(i,j)))
    #vertical neighbours:
    for i in range(len(lines)-1):
        for j in range(len(lines[i])):  
            y_adjacent_down = lines[i][j],lines[i+1][j]
            y_adjacent_up = lines[i+1][j],lines[i][j]
            if check_climb(y_adjacent_down[0], y_adjacent_down[1],val_dict) == True:
                arclist.append(((i,j),(i+1,j)))
            if check_climb(y_adjacent_up[0], y_adjacent_up[1],val_dict) == True:
                arclist.append(((i+1,j),(i,j)))
    return arclist

def check_climb(start,goal,val_dict):
    return bool(re.search(goal,val_dict[start]))

def build_valid_dict():
    pattern = 'S' + string.ascii_lowercase + 'E'
    valid_dict = {}
    for i in range(len(pattern)):
        # Damn this one took me a while, reading is fun:
        valid_dict[pattern[i]] = pattern[:i+2]
    return valid_dict

def build_valid_reverse():
    pattern = 'S' + string.ascii_lowercase + 'E'
    pattern = pattern [::-1]
    valid_dict = {}
    for i in range(len(pattern)):
        # Damn this one took me a while, reading is fun:
        valid_dict[pattern[i]] = pattern[:i+2]
    return valid_dict
    
def add_costs(arc_list):
    cost = {}
    for items in arc_list:
        cost[items] = 1
    return cost

def build_adjacency_list(nodes, arcs):
    adj = {}
    for i in nodes:
        adj[i] = []
    for (i,j) in arcs:
        adj[i].append(j)
    return adj

def dijkstra(adj,c,s):
    nC = len(adj)*max(map(abs,c.values()))

    d = {}
    pred = {}
    for i in adj:
        d[i] = nC
    d[s] = 0
    pred[s] = False

    LIST = set(adj.keys()) #shallow copy of nodes
    while LIST:
        di = nC+1
        for j in LIST:
            if di > d[j]:
                di = d[j]
                i = j
        LIST.remove(i)
        for j in adj[i]: 
            if d[j] > d[i] + c[(i,j)]: 
                d[j] = d[i] + c[(i,j)] 
                pred[j] = i
    return d, pred


##################
#   Main         #
##################


if __name__ == '__main__':

    # Read in the data: 
        
    with open('input.txt') as f:
        lines = f.read().splitlines()   

    # Build the node list, find the starting and end point:
      
    node_list,S,E = make_nodes(lines)
    
    print("Part 1:\n\nThe number of nodes in the mountain is: %d\n" % (len(node_list)))
    
    # Build the arc list:
        
    val_dict = build_valid_dict()
    arc_list = make_arcs(lines, val_dict)
    
    print("The number of arcs in a is: %d\n" % (len(arc_list)))
    
    # Adding the costs:
        
    cost_dict = add_costs(arc_list)

    # Build the adj dictionary:
        
    adj_dijkstra = build_adjacency_list(node_list, arc_list)
    
    # Implement the dijkstra algo:
        
    d, pred = dijkstra(adj_dijkstra, cost_dict, S)
    
    print('The shortest path to the top is %s steps long.\n' % (d[E]))
    
    # Drawing the Path:
        
    pathlist = []
    pathdict = {}
    marker = E
    counter = 0
    
    while pred[marker] != False:
        pathlist.append(marker)
        pathdict[counter] = marker
        marker = pred[marker]
        counter += 1
 
    crt_lines = len(lines)
    crt_pixel_per_line = len(lines[0])
    crt = []
    
    for i in range(crt_lines):
        for j in range(crt_pixel_per_line):
            if (i,j) in pathdict.values():
                crt.append(lines[i][j])
            else:
                crt.append('.')
            
        print(''.join(crt[i*crt_pixel_per_line:(i+1)*crt_pixel_per_line]))   

    
    
    ##############
    # Part b:    #
    ##############
    
    
    a_list = find_letter('a')    
    
    val_dict_rev = build_valid_reverse()
    arc_list_rev = make_arcs(lines, val_dict_rev)
    
    print("\n\nPart 2:\n\nThe number of arcs in a is: %d\n" % (len(arc_list)))
    
    # Adding the costs:
        
    cost_dict_rev = add_costs(arc_list_rev)

    # Build the adj dictionary:
        
    adj_dijkstra = build_adjacency_list(node_list, arc_list_rev)
    
    # Implement the dijkstra algo:
        
    d_rev, pred_rev = dijkstra(adj_dijkstra, cost_dict_rev, E)
    
    min_path = 10000
    min_coord = "error"
    
    for items in a_list:
        if d_rev[items] < min_path:
            min_path = d_rev[items]
            min_coord = items
            
    print('The shortest scenic path to the top is %s steps long and begins at %s.\n' % (min_path,min_coord))

    # Drawing the Path:
        
    pathlist_rev = []
    pathdict_rev = {}
    revmarker = min_coord
    counter = 0
    
    pred_rev[min_coord]
    
    while pred_rev[revmarker] != False:
        pathlist_rev.append(revmarker)
        pathdict_rev[counter] = revmarker
        revmarker = pred_rev[revmarker]
        counter += 1
    
    crt_lines = len(lines)
    crt_pixel_per_line = len(lines[0])
    crt = []
    
    for i in range(crt_lines):
        for j in range(crt_pixel_per_line):
            if (i,j) in pathdict_rev.values():
                crt.append(lines[i][j])
            else:
                crt.append('.')
            
        print(''.join(crt[i*crt_pixel_per_line:(i+1)*crt_pixel_per_line])) 

    
    
    
