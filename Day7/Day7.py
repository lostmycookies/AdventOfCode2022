# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:21:21 2022

@author: lostmycookies
"""


import re
import ast
from collections import deque
import networkx as nx
from pyvis.network import Network
from collections import deque

# Set the variables for the required data structure:

arcs = []
nodes = ['/']  
pointer = deque('/')

# Read in the file:

with open('input.txt') as f:
    lines = f.read().splitlines()

# Remove the first line for easier automation:
    
lines = lines[1:]

for items in lines:
    # find all the nodes:
    if items[0] != '$':
        filesplit = re.split(' ', items)
        if items[0].isdigit():
            nodes.append({filesplit[1]:filesplit[0]})
        else:
            nodes.append("".join(pointer) + filesplit[1])
        
    # build the arcs:
    if items[0:4] == '$ cd':
        if items[-1] != '.':
            filesplit = re.split(' ', items)
            dirnav = filesplit[2]
            arcs.append(("".join(pointer),"".join(pointer)+dirnav))
            pointer.append(dirnav)
        else:
            pointer.pop()
    if items[0].isdigit():
        filesplit = re.split(' ', items)
        arcs.append(("".join(pointer),{filesplit[1]:filesplit[0]}))

##################################
#   Graphical representation     #
##################################
    
# Loading the data into a network:    

def save_node_adding(DiGraphObject, nodes):
    for items in nodes:
        DiGraphObject.add_node(str(items))
    return DiGraphObject

G1 = nx.DiGraph()
G1.add_node('/') # needs to be manually added
save_node_adding(G1, nodes)
 
for start_node,end_node in arcs:
    G1.add_edge(str(start_node),str(end_node))

#### Draw the flow Tree: ####
    
net = Network(notebook=True, directed=True)
    
net.from_nx(G1)    
net.show("DirTree.html")  

###########################################
#   Make Dictionaries with descendants    #
###########################################

# Generate a list with a certain type:
    
def type_list_generator(inputlist,desired_type):
    templist = []
    for items in inputlist:
        if isinstance(items, desired_type):
            templist.append(items)
    return templist

# Get all directories:

dirlist = type_list_generator(nodes, str)

# Finally make a dirsize dictionary:

dirsize = {}

nx.descendants(G1, '/')

for items in dirlist:
    children = nx.descendants(G1, items)
    children = type_list_generator(children, str)
    templist = []
    for entries in children:
        if entries[0] == '{':
            # Had to bring the strings back into dictionary type
            templist.append(ast.literal_eval(entries))
    dirsize[items] = templist
    
# Build a resultdict with the sums of the substructure:

def flatten(l):
    return [item for sublist in l for item in sublist]    

resultdict = {}    

for items in dirsize:
    sizelist = []
    counter = 0
    for entries in dirsize[items]:
        sizelist.append(list(entries.values()))
    # Flatten and turn elements into integer:
    sizelist = [int(item) for sublist in sizelist for item in sublist]
    resultdict[items] = sum(sizelist)
    
max_value = 10**5
totalsum = 0

for key,value in resultdict.items():
    if value < max_value:
        totalsum += value
        
print("\nThe sum of total sizes based on the condition is %s." % (totalsum))
    
###########################################
#   Part b, save harddisk space           #
###########################################

total_available = 70000000 #70 million
unused_needed = 30000000 #30 million
total_used = resultdict['/']

free_space = total_available - total_used
needed_space = unused_needed - free_space

needed_space # 6.5 millions

smallest_value = ['errorerror',70000000]

for key, value in resultdict.items():
    if value > needed_space:
        if value < smallest_value[1]:
            smallest_value[0] = key
            smallest_value[1] = value

print('\nThe smallest value to clear the condition is %s.' % (smallest_value[1]))


