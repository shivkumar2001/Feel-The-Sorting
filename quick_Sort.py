#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:52:16 2021

@author: shiv
"""

import time
import colors as c

def partition(data, start, end, drawData, timeTick):
    i = start + 1
    pivot = data[start]

    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def quick_sort(data, start, end, drawData, timeTick):
    if start < end:
        pivot_position = partition(data, start, end, drawData, timeTick)
        quick_sort(data, start, pivot_position-1, drawData, timeTick)
        quick_sort(data, pivot_position+1, end, drawData, timeTick)

        drawData(data, [c.PURPLE if x >= start and x < pivot_position else c.YELLOW if x == pivot_position
                        else c.DARK_BLUE if x > pivot_position and x <=end else c.BLUE for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, [c.BLUE for x in range(len(data))])