# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:28:37 2025

@author: paredesh3418
"""

def calcMean(alist):
    return sum(alist)/len(alist)

measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]
mean = calcMean(measures)
print('Mean = ', mean)

