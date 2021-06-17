#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:57:00 2021

@author: shiv
"""

import time
import colors as c

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)-1):
        minimum = i
        for k in range(i+1, len(data)):
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        drawData(data, [c.YELLOW if x == minimum or x == i else c.BLUE for x in range(len(data))] )
        time.sleep(timeTick)
        
    drawData(data, [c.BLUE for x in range(len(data))])