# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

names = ['Chris', 'Sussie','Jessica','Simon']

# scenario 1 , need to print out content
print("\nScen 1")
for name in names:
    
    print(name)
    
# scenario 2 , need to print out indexes
print("\nScen 2")
for i in range(len(names)): # range only takes numbers(int)
    
    print(i)

# scenario 3 , need to print out indexes and content
print("\nScen 3")
for i in range(len(names)): # range only takes numbers(int)
    
    print(i, names[i])
# OR
print("\nScen 3 option2")
for i, name in enumerate(names): # range only takes numbers(int)
    
    print(i, name)
    
# print content of nested list , first list has names , second has scores
stu_scores = [['Chris', 'Sussie','Jessica','Simon'],[98, 85,99,100]]
    
print("\nScen 4 nested list")

for row in stu_scores:
    
    for col in row: # inner loop prints content of each row
        
        print(col, end="\t")
    print() # this print statements seperates the rows