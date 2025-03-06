# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:24:34 2025

@author: paredesh3418
"""

import GradesExample as gr

def main():
    
    first , last = gr.welcome()
    
    greet(first, last)
    
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    
    # add numbers
    total = num1 + num2
    print(total)

def  greet(first, last):
    
    print("Hello", first, last)

def welcome():
    '''
    Fuction doesn't require arguments.
    Asks user to enter their name and says hi to them.
    '''
    
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    print()
    
    return first, last
    
main()