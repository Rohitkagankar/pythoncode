#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 08:38:51 2023

@author: rohitkagankar
"""

import os
import time
repeatetime=3600
while True:
    command="osascript -e \'say \"hey rohit drink water\"\'; osascript -e \'display alert \"hey rohit drink water\"\'"
    os.system(command)
    time.sleep(repeatetime)