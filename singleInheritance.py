#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:29:36 2023

@author: rohitkagankar
"""
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def makesound(self):
        print("animal make sound.")
        

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="dog")
        self.breed=breed
    
    def makesound(self):
        print("bark...")
        
a=animal("dog1","dog")
a.makesound()

b=dog("dog", "dog")
b.makesound()