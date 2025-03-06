'''
names = ['Sammy', 'Johnson', 'Jessica', 'Sara']

# enumerate best used to find a index value of a value. 
for i, value in enumerate(names):
    print(i, value)
'''
    
'''
Same as above just different format
    
for i in range(len(names)):
    print(i, names[i])
'''

# Rows, Columns =  grades[][]
grades = [[45, 85, 60] ,[100, 98, 95] ,[85, 91, 90]]

print(grades)

# Iterate list
for rowI in range(len(grades)):
    
    # Display the content of each row.
    # print(row)
    
    for i, col in enumerate(grades[rowI]):    
        
        print()
        print("Before:", col)
        # Adds 5 to that value.
        grades[rowI][i] += 5
        
        # Display the content of each column.
        # End = define how you want to 
        print(col)
        
    print()
print(grades)
    
# Tuples - like a list but can't make any changes like a list.
    
