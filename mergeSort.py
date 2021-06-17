#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 08:42:20 2021

@author: shiv
"""

import time
import colors as c

def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid+1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)

        drawData(data, [c.PURPLE if x >= start and x < mid else c.YELLOW if x == mid 
                        else c.DARK_BLUE if x > mid and x <=end else c.BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [c.BLUE for x in range(len(data))])
    