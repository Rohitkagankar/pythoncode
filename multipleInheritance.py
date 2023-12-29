#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 18:49:28 2023

@author: rohitkagankar
"""

class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name of employee is {self.name}.")

class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}.")

class empDancer(employee,dancer):
    def __init__(self, dance,name):
        self.dance=dance
        self.name=name

a=empDancer("lavani", "radha")
print(a.dance,a.name)
a.show()
dancer.show(a)
print(empDancer.mro())



    