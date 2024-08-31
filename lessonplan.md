# Lesson plan
  
Operations

**Introduce Data Types:**

Integer
Float (Similar to double)
Strings
Booleans

**Operators**

+ addition
- subtraction
* multiplication
** exponent
/ division (float result)
// division (int result)
% mod (remainder)

**Variables**

Assigning to variables
Reassigning(overwriting) to variables
Calling variables

Example Lesson:

'''
Lesson 2 - Data Types, Variables, Operators
Author: Mr. Kalisz
Date Created: September 4th, 2023
Date Last Modified: September 4th, 2023
'''

#Data Types

#Integer - Whole numbers, numbers without decimal points

print(5)

#Float - Decimal numbers.  Numbers that alwasy have decimal points.

print(4.5)

print(5.0)

#Strings - text.  Text can anything on the keyboard or more.
#Strings are always contained in quotation marks
#Strings are named such becuase they are a string of characters

print("These are strings")
print("12345")

#Booleans - True or False.  These will be talked about more later in the course. They do NOT need quotations.
print(True)
print(False)

#Variables

#Variables are like containers that hold information
#They are sections in memory that store information of a certain type

#variable goes on the left, the value you want to asssign it goes on the right
num = 4  #assignment statement, stores an integer in the variable num

num2 = 9.5 #this is a variable that stores a float
num2 = 10.3 #You can overwrite variable by assigning to them again.  Any code after this line will use the most recent value of num2.

#floats and integers are always different, even if they seem they have the same value.

word = "Hello" #This is a string stored in a variable
text = "12345" #ANY character can go in a string. and must be surrounded by quotations.

#word = "Bye" # This will replace the value of word with "Bye" instead of "Hello"

#Calling a variable

print(word) #Variable calls replace the variable with its value.

#Variable calls happen anytime the value is not on the left side of an assignment statement.

#Operators - only used on integers and floats

# addition(+), subtraction(-), Multiplication(*), Division(/), Integer Division(//), Mod(%)

#addition

num4 = 5 + 9 #Assigns 14 to num4
print(num4)

#subtraction

num5 = 10 - 6 #Assigns 4 to num5
print(num5)

#Multiplication

num6 = num5 * 4 #Assigns 16 to num6

#Division

num7 = num6 / 5 #Assigns 3.2 to num7
print(num7)

#Integer Division (or floor division)

num7 = num6 // 5 #Rounds down to 3.  Always gets rid of the decimal point.
print(num7)

#Mod (Remainder)
num7 = num6 % 5
print(num7)