#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:23:05 2023

@author: rohitkagankar
"""

#walrus operator
a1=True
print(a1:=False)

a=[11,22,33,44,55,66]
while (n:=len(a))>0:
    print(a.pop())

#without walrus operator    
foods=list()
while True:
    food=input("what food do you like?")
    if food =="quite":
        break
    foods.append(food)
print(foods)
    
#with walrus operator
foodss=list()
while (food:=input("what food do you like?"))!="quite":
    foodss.append(food)
print(foodss)

        