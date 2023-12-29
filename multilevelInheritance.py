#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:57:33 2023

@author: rohitkagankar
"""
class cycle:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the cycle company is {self.name}.")
class motor(cycle):
    def __init__(self,name,model):
        cycle.__init__(self,name)
        self.model=model
    def show(self):
        cycle.show(self)
        print(f"model:{self.model}")
class car(motor):
    def __init__(self,name,color):
        motor.__init__(self,name,model="2020")
        self.color=color
    def show(self):
        motor.show(self)
        print(f"color :{self.color}")

a=car("hero","blue")
a.show()






class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show_details(self):
        print(f"name= {self.name}")
        print(f"species= self.species")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    def show_details(self):
        Animal.show_details(self)
        print(f"breed= {self.breed}.")

class GoldenRetrival(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name,breed="GoldenRetrival")
        self.color=color
    def show_details(self):
        Dog.show_details(self)
        print(f"color={self.color}.")
        
a=GoldenRetrival("Dognew", "white-black")
a.show_details()
