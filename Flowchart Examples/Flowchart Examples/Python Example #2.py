# Get the salary

salary = float(input("Enter salary: "))

# Evaluate score

# Add underscore if you want to read it better
if salary >= 30_000:
    
    # Ask for # years
    years = int(input("Enter years worked: "))

    if years >= 2:
        
        # if true, they get the loan
        print("Qualified!! You get the loan!")

    else:

        print("Not approved.")
        print("Haven't worked for 2 or more years.")

else:
    print("Not approved.")
    print("You don't make enough...")
