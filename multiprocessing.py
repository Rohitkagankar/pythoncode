#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:58:38 2023

@author: rohitkagankar
"""

import multiprocessing
import requests

def downloadFile(url,name):
    #print(f"started downloading {name}.")
    response=requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    #print(f"finished downloading {name}")
    
url="https://picsum.photos/2000/3000"
#pros = [ ]
for i in range(5):
    downloadFile(url, i)
    #p= multiprocessing.Process(target=downloadFile, args=[url,i])
    #p.start()
    #pros.append(p)
    
    
#for p in pros:
   # p.join()
    

