#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:13:27 2023

@author: rohitkagankar
"""

import re

#pattern="ram"
pattern=r"[A-Z]an"
text='''dji kjdoi dfsij akld  ra m asj ei sdoij dskn sde ram kd to ndo ram Can Man we Fan'''

#match=re.search(pattern, text)
#print(match)
matches=re.finditer(pattern, text)
for match in matches:
    print(match)