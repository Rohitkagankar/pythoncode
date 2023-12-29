#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 14:58:53 2023

@author: rohitkagankar
"""

import reqests
url="http://jsonplaceholder.typicode.com/posts"
data={
      "title":"rohit",
      "body":"kagankar",
      "userid":66,}
headers={
    'Content-type':'application/json; charset=UTF8',
    }
response=reqests.post(url,headers=header, json=data)
