#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:48:54 2021

@author: shiv
"""

import time
import  colors  as c

def heapify(data, n, i, drawData, timeTick):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest, drawData, timeTick)


def heap_sort(data, drawData, timeTick):
    n = len(data)

    for i in range(n-1, -1, -1):
        heapify(data, n, i, drawData, timeTick)

    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0, drawData, timeTick)
        drawData(data, [c.YELLOW if x == i else c.BLUE for x in range(n)])
        time.sleep(timeTick)
    
    drawData(data, [c.BLUE for x in range(len(data))])
    