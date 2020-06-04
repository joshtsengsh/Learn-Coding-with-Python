#Created by Josh Tseng, 2 June 2020
#This file illustrates how to loop through a dictionary's keys and/or values

phone_numbers = {
"John": "90904454",
"Ellie": "90234056",
"Raj": "94456654"
}

#Example 1: #Using the for loop method of for x in variable method makes the loop iterate through the key values
for item in phone_numbers:
    print(item)

#Example 2: One way of getting the for loop to iterate through the values instead is to do the following
#Note that there are many other valid methods to achieve the same results, this is just one of them
for item in phone_numbers:
    print(phone_numbers[item])


