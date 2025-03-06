
# Declaring a list

L = [1, "a" , "a", "string" , 1+2]

# printing a list
print("Declaring a list ")
print (L)

# print list element using a loop
print()# this statement is used to skip a line
print("printing elements using for loop")
for item in L:

    print(item)

print()# this statement is used to skip a line
# print an element
print("Print individual element in list ")
print (L[1] ) # notice we defined the index of the emlement we want to print

''' 2 ways to add an element to a list
 method 1) append , this adds to end of list'''

# appending
print("Appending list, item 6 added ")
L.append(6) 
print( L )

''' method 2) insert, here we define the position(index)/location

for the element we are adding'''
# inserting
print("inserting element 'b' in position 1 ")
L.insert(1,"b")
print( L )


# deleting elements from a list
''' there are three ways to delete elements from a list
1) pop() method, when not passed arguements itdeletes from the end of the list '''
print("Using pop mentod to delete from end of list ")
L.pop() 
print( L )

# when passed an regument (index number) , it removes element in that position 

print("Using pop method to delete element in position 1 ")
L.pop(1)
print( L )

''' 2) remove() method , this would remove the element we define
regardless of it's location '''
# note that if there are several instances of the element

print("Using remove mentod to delete element 'a' ")

L.remove('a')
print( L )

'''del , here we would define the index of the element we want to delete'''
print("Using delete to remove element in position 2 ")
del L[2]
print( L )
