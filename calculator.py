"""
Program: Simple Calculator 
Author: Arif yacop
Simple calcuatro help the user calculate the basic 4 operations including:
addition, subtraction, multiplication and division
Significant constants
         there is no constants
 2. The inputs are
         2 numbers (at least)
 3. Computations:
         addition: number + another number
         subtraction: number - another number
         multiplication: number * another number
         division: number / another number
 4. The outputs are
         computation result
"""

def add (x, y):
    return(x + y)

def subtract(x, y):
    return(x - y)

def multiply(x, y):
    return(x * y)

def divide(x, y):
    return(x / y)

def input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That was not a number")

# Keep going around the loop until the user chooses 5 to quit

while True:
    print
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Quit")

    choice = input("Enter choice(1/2/3/4/5):")

    # Do they want to quit?

    if choice == 5:
        break

    num1 = input_number("Enter first number: ")
    num2 = input_number("Enter second number: ")

    if choice == 1:
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == 2:
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == 3:
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == 4:
        print(num1,"/",num2,"=", divide(num1,num2))

    else:
        print("%s - Invalid input" % choice)