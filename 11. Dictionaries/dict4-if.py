#Created by Josh Tseng, 2 June 2020
#This file illustrates how if-statements can be used to determine if a key exists in a dictionary

phone_numbers = {
"John": "90904454",
"Ellie": "90234056",
"Raj": "94456654"
}

print("Welcome! Search for a person's phone number.")
user_search = input("Type a person's name: ")

if user_search in phone_numbers:
    print("The phone number for " + user_search + " is: " + phone_numbers[user_search])
else:
    print("No result for a person named " + user_search + " was found in our database")

#Note: The search must be an exact match, meaning it is also case sensitive
#e.g. A search for "Raj" (with a capital R) would produce a result, but a search for "raj" (without the capital R) would not show his phone number

print("---")

#How does this work?
#The code "user_search in phone_numbers" will produce a Boolean value that is either true or false
#See for yourself with the code below
print(user_search in phone_numbers)
