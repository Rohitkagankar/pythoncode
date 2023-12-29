#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 08:32:56 2023

@author: rohitkagankar
"""
import time
def even():
    j=0
    for i in range(500):
        if i%2==0:
            print(i)
            j+=1
    print("total even no are",j)


def odd():
    i=0
    j=0
    while i!=500:
        if i%2!=0:
            print(i)
            j+=1
        i+=1
    print("total odd no are",j)

init=time.time()
print(init)
b=even()
print(time.time()-init)
init=time.time()
a=odd()
print(time.time()-init)

t=time.localtime()
timeFormat=time.strftime("%Y-%m-%d  %H:%M:%S")
print(timeFormat)
print(t)

        
            