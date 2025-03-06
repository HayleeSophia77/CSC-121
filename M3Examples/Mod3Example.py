# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:39:37 2025

@author: paredesh3418
"""

scores = [100,85.5,78,60,75,80,82,71]
numbers = []

# .append = add a value to the end of a list
# .insert(,) = insert a value to a certain index
# index =  the place a value is at in a list. Starts at Zero.
# len() = gets the length of a list
# .count() = counts how many of that value is in the list.
# .index() = gets the index position that a value is in.
# .pop() =  removes a value.
# .remove() = removes a value
# del __ = delete a list
# .extend() = add more value(s) to a list after the last value. 

'''
print(f'{"Num":<7}{"Sqr"}')
print('-'*14)

numbers = [5,6,7,8,9,10]

for num in numbers:
    sqr = num**2 
    print(f'{num:<7}{sqr}')
'''

numbers = [98,78,84,78,100]

'''
print('Before')
'''

print(numbers)

value = 78
indexes = []

'''
for x in numbers:
    
    if x == value:
        
        # Delete
        i = numbers.index(x)
    
        numbers.remove(x)
        
        # Add it to the list
        indexes.append(i)
'''    
for x in range(len(numbers)):
    
    if numbers[x] in range
        
        # Delete
        # Add it to the list
        indexes.append(x)
        
    
print('\nAfter')
print(indexes)
print(numbers)