# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:20:12 2025

@author: paredesh3418
"""

scores = [98,100,81,54]
names = ['Sammy', 'Johnson', 'Jessica', 'Sara']

for i in range(len(scores)):
    
    # Evaluate the score
    if scores[i] >= 90:
        print(names[i], 'A')
        
    elif scores[i] >= 80:
        print(names[i], 'B')
        
    elif scores[i] >= 70:
        print(names[i], 'C')
        
    elif scores[i] >= 60:
        print(names[i], 'D')
    
    else:
        print(names[i], 'F')