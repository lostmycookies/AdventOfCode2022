# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:00:01 2022

@author: lostmycookies
"""


with open('input.txt') as f:
    lines = f.read().splitlines()  

result = ''    

for items in lines:
    cut = len(items)//2
    string1 = items[0:cut]
    string2 = items[(cut):len(items)]
    common = ''.join(set(string1).intersection(string2))
    result += common

score = [ord(char) - 96 for char in result]   

final_result = 0

for i in range(len(score)):
    if score[i] < 0:
        final_result += score[i] + 58
    else:
        final_result += score[i]
    
print("The final result is %d." % (final_result))