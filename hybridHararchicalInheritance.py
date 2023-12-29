#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 21:05:49 2023

@author: rohitkagankar
"""
#hybrid inheriance
class friute:
    def show():
        print("It include all fruites.")

class Apple(friute):
    def show():
        friute.show()
        print("the Apple is very nice fruite.")

class new:
    def show():
        print("this is fruite family.")
        
class juice(Apple,new):
    def show(self):
        new.show()
        Apple.show()
        print("All fruites are used to make juice.")

a=juice()
a.show()

#hirarchical inheritance------

class mainclass:
    def show():
        print("this is main class.")
class derivedclass1(mainclass):
    def show():
        mainclass.show()
        print("this is derived class 1")
        
class derivedclass2(mainclass):
    def show():
        mainclass.show()
        print("this is derived class2.")
class subderived1(derivedclass1):
    def show(self):
        derivedclass1.show()
        print("this is subderived class 1.")
class subderived2(derivedclass1):
    def show(self):
        derivedclass1.show()
        print("this is subderived class 2.")

a=subderived1()
a.show()
b=subderived2()
b.show()