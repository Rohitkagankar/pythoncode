#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:31:08 2023

@author: rohitkagankar
"""
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __add__(self,x):
        return vector(self.i+ x.i,self.j+x.j,self.k+x.k)

a1=vector(4, 5, 6)
print(a1)
a2=vector(2,3,4)
print(a2)
print(a1+a2)
print(type(a1+a2))

#-------another example------------

class calculator:
    def __init__(self,a):
        self.a=a
    def show (self):
        print(f"the value of element is: {self.a}")
    def __add__(self,y):
        return self.a+y.a

a1=calculator(5)
a1.show()
a2=calculator(3)
a2.show()
print(a1+a2)
print(type(a1+a2))