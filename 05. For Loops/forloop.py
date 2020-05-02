#Created by Josh Tseng, 1 May 2020
#This file illustrates how you can use a basic for loop to repeat a certain action

#Step 1: Writing a for loop

for i in range (0, 5):
    print(i)

#Step 2: Take note of certain things:
a) For loops, like some other things you will see later in Python, must have the code inside be indented.
Anything not indented will not be performed in the for loop.
b) The i in for i in range is a variable. It is storing the value counting from 0 to 4.
You will see this demonstrated when you run the code and see the output.
c) The range in the brackets goes in an inclusive, exclusive format.
In the example for i in range (0, 5), it is counting from 0 to 5, including 0 and excluding 5.
This is why the displayed numbers stop at 4; the range only goes up to 4.
