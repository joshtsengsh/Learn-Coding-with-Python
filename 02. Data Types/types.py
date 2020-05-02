#Created by Josh Tseng, 1 May 2020
#This file will illustrate some key data types in Python

#Integer
#Integers are all whole numbers (no decimals) and are not declared using quotation marks
#Python will show you that the number 100 is an integer by telling you it is an "int"
print("Integer value:")
print(100)
print(type(100))

#String
#Strings are declared using quotation marks, either the single quote ' ' or the double quotes " "
#Python will tell you that the text "Hi Mr Rogers" is a string by telling you it is a "str"
print("String values:")
print("Hi Mr Rogers")

#Using single quotation marks:
print(type('Hi Mr Rogers'))

#Using double quotation marks:
print(type("Hi Mr Rogers"))

#Strings that hold numerical values are still text strings, as seen in this example
#print("500")
print(type("500"))

#Boolean
#In short, Boolean values are true or false
#In Python, make sure the first letter of the value is capitalised (i.e. False with capital F, and True with capital T)
print("Boolean values:")
print(True)
print(type(True))
print(False)
print(type(False))

#Float (numerical decimals)
#Float values are used to handle numbers with decimal points
print("Float value:")
print(0.05)
print(type(0.05))

#Food for thought:
#What would happen if we only had type(100) instead of print(type(100))?
#Answer: Nothing would be seen on the terminal; you need a print statement to see what the computer has to tell you