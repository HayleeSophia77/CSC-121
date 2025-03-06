

'''

# Get the bill amount and the tip percentage

# (Gets information, allows user to enter information)
b_a = input("Enter bill amount $")

# Get the percenage
t_p = input("Enter tip percentage (0.15 for 15%): ")

#Calculate the tip and total
tip = b_a * t_p

total = b_a + tip

# Show result

print("Total to be paid $", total)

THIS GIVES AN ERROR

CAN'T MULTIPLY SEQUENCE BY NON_INT OF TYPE 'str'

'''

'''
# Get the bill amount and the tip percentage

# (Gets information, allows user to enter information[input]. Creates a variable[float].)

b_a = float(input("Enter bill amount $"))

# Get the percenage

t_p = float(input("Enter tip percentage (0.15 for 15%): "))

# If < 15%, apply 20%

if t_p < 0.15 :

    t_p = 0.20
    
    print("Tip enter is below 15%!!! Therefore 20% has been applied!")
    
else: # Thank the User

    print("Thank you for the generous tip")

#Calculate the tip and total

tip = b_a * t_p

total = b_a + tip

# Show result

# Rounds the variable two decimal points(round)
# seperates the arguments or doesn't leave a space. sep='' takes away a space.
print("Total to be paid $", round(total), sep='')
'''

# Get the bill amount and the tip percentage

# (Gets information, allows user to enter information[input]. Creates a variable[float].)

b_a = float(input("Enter bill amount $"))

# Get the percenage

t_p = float(input("Enter tip percentage (15%, 20% or 25%): "))

# Evaluate tip
if t_p < 15 :
    
    t_p = 0.15
    
elif t_p == 20:

    t_p = 0.20

elif t_p == 25:

    t_p = 0.25

elif t_p <15:

    t_p = 0.20
    print("Tip enter is below 15%!!! Therefore 20% has been applied!")
    
else: # Thank the User
    
    print("Thank you for the generous tip")
    t_p = t_p / 100

#Calculate the tip and total
tip = b_a * t_p

total = b_a + tip

# Show result

# Rounds the variable two decimal points(round)
# seperates the arguments or doesn't leave a space. sep='' takes away a space.
print("Total to be paid $", round(total), sep='') 

