#Created by Josh Tseng, 5 May 2020
#This file illustrates how if statements are used in Python

#Showing a basic if statement
#The programme asks the user to tell it how much money the user has, then prints out a statement showing the user's amount of money indicated.
#If the user enters "0", the programme will also print out an additional cheeky statement.

user_input = input("Tell me how much money you have: ")

print("You have $"+user_input)

#Note that the contents of line 14 are indented
if user_input=="0":
    print("Wow, you have nothing!")

#Food for thought: on line 13, the number 0 is in quotation marks, why?
#This is because the input() function always provides a string, and the user_input variable's contents has never been converted to an integer.
#The == sign is used to find out if two values are equal to one another
#The opposite of the == is !=
