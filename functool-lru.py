#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 17:25:09 2023

@author: rohitkagankar
"""

import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return 5*n

print(fx(10))
print("done with 10.")
print(fx(5))
print("done with 5")

print(fx(10))
print("done with 10.")
print(fx(5))
print("done with 5")

print(fx(10))
print("done with 10.")
print(fx(5))
print("done with 5")
