#Created by Josh Tseng, 2 June 2020
#This file illustrates how dictionaries are created, and how they work

#Dictionaries are used to associate a so-called "key" with a corresponding "value"
#Dictionaries are created using the curly brackets (also called braces) which are the { }
#The format to create dictionaries is {key: value}

phone_numbers = {
"John": "90904454",
"Ellie": "90234056",
"Raj": "94456654"
}

#Print the dictionary
print(phone_numbers)
print(type(phone_numbers))

#Why do you need dictionaries?
#They help in cases where it's convenient to use a unique name (the key) to connect to a specific set of values
#Example: What is Raj's phone number?
print("Raj's phone number:")
print(phone_numbers["Raj"])

