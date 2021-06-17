#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 08:41:37 2021

@author: shiv
"""

# We need the time module to create some time difference between each comparison
import time

# Importing colors from colors.py
import colors as c

def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [c.YELLOW if x == j or x == j+1 else c.BLUE for x in range(len(data))] )
                time.sleep(timeTick)
                
    drawData(data, [c.BLUE for x in range(len(data))])
    