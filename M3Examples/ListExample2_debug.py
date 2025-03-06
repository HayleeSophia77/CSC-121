def main():
    
    #Creates empty lists
    numList = []
    wordList = []

    # Display to user what the program does.
    print("This program allows user to create a list containing either numbers or string, it then evaluates content and eliminates duplicates")

    # Display to the user to start with the list of numbers.
    print("\nLet us start with the number list")

    # Allow user to enter numbers as an integer. How many to add to list?
    number = int(input("\nHow many numbers do you want to add to list? "))

    # 
    for x in range(number): # Range can only handle integers not floats
        num = input(f"Enter element number {x+1}: ")
        numList.append(num)


    print("\nNow we move on to list of words/string")

    # How many do you want to add to the list?
    number = int(input("\nHow many elements do you want to add to list? "))

    #
    for x in range(number):
        word = input(f"Enter element number {x+1}: ")
        wordList.append(word)
        # print the two lists

    # pass list to function

    dis_results(numList, wordList)

# Display both lists
def dis_results(numList, wordList):
    print("Original Number list:", numList)
    print("\nList without duplicates:", unique(numList))
    print()

    print("Original Word list:", wordList)
    print("\nList without duplicates:", unique(wordList))
    print()

                
def unique(values):

    '''no code added here,
    add code that iterates over a list that can have duplicates
    the is to delete any duplicates and return a list that has no
    duplicates

    You are to use LIST ONLY , not sets
    '''
    # Itereate = loop.
    
    # Create an empty list for no duplicates.
    no_dupe = []
    
    # 
    for x in values:
        
          #         
          if x not in no_dupe:
              
              # (Add the element to new list) Append no duplicates.
              no_dupe.append(x)
              
    # Return no duplicates          
    return no_dupe
                   
              
main()
