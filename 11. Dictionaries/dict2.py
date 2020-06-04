#Created by Josh Tseng, 2 June 2020
#This file illustrates how you can manipulate dictionaries

phone_numbers = {
"John": "90904454",
"Ellie": "90234056",
"Raj": "94456654"
}

#How do you add an entry into the dictionary?
#Example: Add a person named Farah with the phone number 81818181
phone_numbers["Farah"] = "81818181"
#See the updated phone_numbers dictionary by printing it
print("Added Farah and her phone number:")
print(phone_numbers)

#Change the value associated with a specific key
#Example: Change John's phone number to 93939393
phone_numbers["John"] = "93939393"
#See the updated phone_numbers dictionary
print("Edited John's number:")
print(phone_numbers)
