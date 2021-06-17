#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:50:33 2021

@author: shiv
"""

import time
import colors as c

def insertion_sort(data, drawData, timeTick):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k-1]:
            data[k] = data[k-1]
            k -= 1
        data[k] = temp
        drawData(data, [c.YELLOW if x == k or x == i else c.BLUE for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, [c.BLUE for x in range(len(data))])