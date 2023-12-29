#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 17:02:29 2023

@author: rohitkagankar
"""

def my_generator():
    for i in range(100):
        yield i

a1=my_generator()
print(next(a1))
print(next(a1))

for i in a1:
    print(i)