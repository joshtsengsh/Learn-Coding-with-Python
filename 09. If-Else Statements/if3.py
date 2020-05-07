#Created by Josh Tseng, 5 May 2020
#This file illustrates how an if-else chain can be created with "elif" statements, standing for "else if"
#This is used for more complex logic handling

user_string = input("Please enter a line of text: ")

#How long is this string?
str_len = len(user_string)

print("Your string's length is "+str(str_len)+" characters long.")

if str_len <= 15:
    print("You sure don't say much...")
elif str_len <=35:
    print("Aha! A sufficient length of string.")
else:
    print("Wow, you are long-winded...")

#Food for thought: What will happen if you swapped lines 12 and 14?
#Also: How long would the length of the string have to be for the programme to print the statement on line 17?
#Answer: It would be 36 characters or longer
