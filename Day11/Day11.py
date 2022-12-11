# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:08:22 2022

@author: lostmycookies
"""


import re

with open('input.txt') as f:
    lines = f.read().splitlines()
    
class Monkey:
    
    # Class Variable:
    animal = 'monkey'
    
    # Constructor:
        
    def __init__(self,number,loot,operation,monkeytest,throw,inspections):
        self.number = number
        self.loot = loot
        self.operation = operation
        self.monkeytest = monkeytest
        self.throw = throw
        self.inspections = inspections
        
    # Add instances:
    def setNumber(self,number):
        self.number = number
        
    def setLoot(self,loot):
        self.loot = loot
        
    def setOperation(self,operation):
        self.operation = operation

    def setMonkeytest(self,monkeytest):
        self.monkeytest = monkeytest

    def setThrow(self,throw):
        self.throw = throw
        
    def setInspections(self,inspections):
        self.inspections = inspections
    
    # Call of function adds an inspection
    def addInspection(self):
        self.inspections = self.inspections+1

    # Retrieve instances:   
        
    def getNumber(self):
        return self.number
        
    def getLoot(self):
        return self.loot
        
    def getOperation(self):
        return self.operation
        
    def getMonkeytest(self):
        return self.monkeytest
    
    def getThrow(self):
        return self.throw
    
    def getInspections(self):
        return self.inspections
    
        

# Build the parsing:

def monkeybuild(parseinput):
    lines = parseinput
    monkeydict = {}
    
    for i in range(0,len(lines),7):
        monkeynumber = i // 7
        # Parse the individual components:
        temp_number = re.findall('\d+', lines[i])
        temp_items = re.findall('\d+', lines[i+1])
        temp_operation = re.split(' ',lines[i+2])[-3:]
        temp_test = re.findall('\d+', lines[i+3])
        temp_throw = [re.findall('\d+', lines[i+4]),re.findall('\d+', lines[i+5])]
        # Build the monkeydict:
        monkeydict[monkeynumber] = Monkey(temp_number,temp_items,temp_operation,temp_test,temp_throw,0)
    return monkeydict

def monkeyround(monkeydictinput):
    monkeydict_len = len(monkeydictinput)
    monkeys = monkeydictinput
    
    for i in range(monkeydict_len):
        for items in monkeys[i].getLoot():
            # Get new stress value:
            old = items
            operation = monkeys[i].getOperation()
            operator = operation[1]
            if operation[2] == 'old':
                new = eval(old + operator + old)
            else:
                new = eval(old + operator + operation[2])
            # Divide by 3:
            new = new // 3
            # Add inspection and decide:
            monkeys[i].addInspection()
            passtest = monkeys[i].getThrow()[0][0]
            failtest = monkeys[i].getThrow()[1][0]
            if new % int(monkeys[i].getMonkeytest()[0]) == 0:
                lootbag = monkeys[int(passtest)].getLoot()
                lootbag.append(str(new))
                monkeys[int(passtest)].setLoot(lootbag)
            else:
                lootbag = monkeys[int(failtest)].getLoot()
                lootbag.append(str(new))
                monkeys[int(failtest)].setLoot(lootbag)
        # Remove the item from the Monkey:
        monkeys[i].setLoot([])
    return monkeys

# Run the functions:

monkeydict = monkeybuild(lines)
result_dict = monkeyround(monkeydict)

rounds = 20

for i in range(rounds-1):
    monkeyround(result_dict)

# Get the most active monkeys:
    
for items in result_dict:
    print('Monkey %s inspected items %s times.' % (items, result_dict[items].getInspections()))
