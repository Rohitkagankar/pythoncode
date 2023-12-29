#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:52:54 2023

@author: rohitkagankar
"""

import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("this is function 1.")
    return "rohit"

async def function2():
    await asyncio.sleep(1)
    print("this is function 2.")

async def function3():
    await asyncio.sleep(1)
    print("this is function 3.")

async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
        )
    print(L)
    #task = asyncio.create_task(function1())
    #await function1()
    #await function2()
    #await function3()

#asyncio.run(main())


    