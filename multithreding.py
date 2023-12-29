#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:23:02 2023

@author: rohitkagankar
"""

import threading
import time

def show(second):
    print(f"the method will be exicute in {second}.")
    time.sleep(second)
time1 = time.perf_counter()
show(3)
show(2)
show(1)
time2 = time.perf_counter()
print(time2-time1)

time3=time.perf_counter()
t1=threading.Thread(target=show, args=[3])
t2=threading.Thread(target=show, args=[2])
t3=threading.Thread(target=show, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time4=time.perf_counter()
print(time4-time3)