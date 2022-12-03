# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:41:35 2022

@author: lostmycookies
"""


with open('input.txt') as f:
    lines = f.read().splitlines()  

result = ''    

string1 = lines[0]
string2 = lines[1]
string3 = lines[2]

common = ''.join(set(string1).intersection(string2).intersection(string3))

for i in range(len(lines))[0:len(lines):3]:
    string1 = lines[i]
    string2 = lines[i+1]
    string3 = lines[i+2]
    common = ''.join(set(string1).intersection(string2).intersection(string3))
    result += common
    
score = [ord(char) - 96 for char in result]   

final_result = 0

for i in range(len(score)):
    if score[i] < 0:
        final_result += score[i] + 58
    else:
        final_result += score[i]
        
print("The final result is %d." % (final_result))