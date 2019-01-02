

# https://www.learnpython.org/
# https://www.datacamp.com/courses/intro-to-python-for-data-science

###################################################################################################################################
## Learn the Basics
###################################################################################################################################


###################################################################################################################################
# Hello World

print("This line will be printed.")


x = 2
if x == 1:
    print("x equals 1")
elif x != 1:
    print("x differs from one")
else:
    print("this should have never happend")


###################################################################################################################################
# Variables and Types

myint = 7
print(myint)


myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)


one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)


a, b = 3, 4
print(a,b)



# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)


# change this code
mystring = "hello"
myfloat = float(10)
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


###################################################################################################################################
# Lists

mylist = []
mylist.append(1)
mylist.append("Hi")
mylist.append(float(4))

for x in mylist:
    if x == "Hi":
        print("Joha")



numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None

second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("Hello")
strings.append("World")

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)


###################################################################################################################################
# Basic Operators


remainder = 11 % 3
print(remainder)


false_squared = 7 ^ 4 # toto je odecitani
print(false_squared)


squared = 7 ** 2
print(squared)
cubed = 2 ** 3
print(cubed)


helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

# Using operators with lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)



x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")



###################################################################################################################################
# String Formatting

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)


# This prints out "John is 23 years old."

# zalezi na poradi prvku, %s nebo %d mi udava v jakem formatu to ma byt - %s asi jako string, %d je number, why???

name = "John"
age = 23
print("%s is %d years old." % (name, age))
print("%d is %s years old." % (age, name))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s"% mylist)

# %s - String (or any object with a string representation, like numbers)
#
# %d - Integers
#
# %f - Floating point numbers
#
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#
# %x/%X - Integers in hex representation (lowercase/uppercase)


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)


###################################################################################################################################
# Basic String Operations


astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

print(astring.index("o")) # First occurence of "o" in string - zacina nulou
print(astring.index("!"))


print(astring.count("l")) # pocet znaku

print(astring[3:7]) # This prints the characters of string from 3 to 7 skipping one character.
print(astring[3:7:3]) # [start:stop:step]

print(astring[::-1]) # Reverse :)

print(astring.upper())
print(astring.capitalize()) # makes upper only first letter
print(astring.lower())


print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))


astring = "Hello world!"
afewwords = astring.split(" ") # Splits into list divided by space

print(afewwords[0])
print(afewwords[1])




s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))



###################################################################################################################################
# Conditions

x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
print(x != 3) # <> v Pythonu není


name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


####### IF STATETENT

# if <statement is="" true="">:
#     <do something="">
#     ....
#     ....
# elif <another statement="" is="" true="">: # else if
#     <do something="" else="">
#     ....
#     ....
# else:
#     <do another="" thing="">
#     ....
#     ....
# </do></do></another></do></statement>


x = 2
if x == 2:
    print("x equals two!")
elif x == 3:
    print("x equal three!")
else:
    print("x does not equal to two nor three.")


#Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. For example:
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


print(not False) # Prints out True



# change this code
number = 20
second_number =  0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array: # pokud v něm něco je tak vrátí true
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number: # pokud má hotnotu nula tak vrátí false...
    print("6")




####### FOR LOOPS

primes = [2, 3, 5, 7, 11]
for prime in primes:
    print(prime)



# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 20, 2): # skace od 3 do 20 po dvou
    print(x)

for x in range(20, 3, -2): # skace od 20 do 3 po dvou dolu
    print(x)


####### WHILE LOOOOOOOOOOOOOOOOOOOOOOOOOPS

# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


# Prints out 0,1,2,3,4
# BREAK
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


# CONTINUE
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0: # % - mod
        continue # skoci zase nahoru
    print(x)


# ELSE IN LOOPS


# unlike languages like C,CPP.. we can use else for loops.
# When the loop condition of "for" or "while" statement fails then code part in "else" is executed.
# If break statement is executed inside for loop then the "else" part is skipped.
# Note that "else" part is executed even if there is a continue statement.

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")



numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for num in numbers:
    if num == 237:
        break
    if(num%2==0):
        print(num)



###################################################################################################################################
# Functions

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


print(my_function_with_args("MACICEK","Ahoj"))

def sum_two_numbers(a, b):
    print ("spočteno") #toto je to co může vykonat
    return a + b # toto je to co funkce vrátí, nemusi vratit nic, pak je to jako procedura


print(sum_two_numbers(1,3))

x = sum_two_numbers(9,8)



# Modify this function to return a list of strings as defined above
def list_benefits():
    return["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()



###################################################################################################################################
# Classes and objects

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myObjectx = MyClass()
myObjecty = MyClass()

x = myObjectx.variable
print(myObjectx.variable)
print(myObjecty.variable)

myObjectx.function()

# We have a class defined for vehicles.
# Create two new vehicles called car1 and car2.
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer
# , and car2 to be a blue van named Jump worth $10,000.00.



# Definice bez argumentů a inicialni nastaveni až ve vnitř v Class
class VehicleClass():
    name = ""
    color = ""
    value = 100.00 # Default values
    type = "car" # Default values

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.type, self.value)
        return desc_str

# Initialize
car1 = VehicleClass()
car2 = VehicleClass()

# Assign values
car1.color = "red"
car1.type = "convertible"
car1.value = 60000.00
car1.name = "Fer"

car2.color = "blue"
car2.type = "van"
car2.value = 10000.00
car2.name = "Jump"

print(car1.color)

# test code
print(car1.description())
print(car2.description())




# Definice objektu pomocí argumentů a __init__ funkce
class VehicleClass2():

    def __init__(self, name, color, value = 0, type="unknown"): # defaultni hodnoty
        self.name = name
        self.color = color
        self.value = value
        self.type = type

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.type, self.value)
        return desc_str


# Initialize
car3 = VehicleClass2("Porsche","Cyan",100000.00)

# test code
print(car3.description())

car3.name = "Range Rover"

# Smaze to cele property
del car3.color
# Smaze objekt
del car3

###################################################################################################################################
# Dictionaries

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

print(phonebook)
print(phonebook["John"])

for name, number in phonebook.items():
    print("Phone number of %s is %d" %(name, number))

# Remove a value

del phonebook["John"]


# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here

phonebook["Jake"] = 938273443
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")


###################################################################################################################################
# Modules and Packages
# Mrknout se na toto ještě víc

# Vytvoreni dvou novych modulu draw.py a game.py


import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))


###################################################################################################################################
# Numpy Arrays

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))


# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)


# For a boolean response
bmi > 23

# Print only those observations above 23
bmi[bmi > 23]


weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg

np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg

kg_to_lbs_conversion_const = 2.2

# Print out np_weight_lbs

np_weight_lbs = np_weight_kg * kg_to_lbs_conversion_const

print(np_weight_lbs)



###################################################################################################################################
# Pandas Basics

# dojet to, spadlo to na importu pandas

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Set the index for brics
# Misto ID radku to hodi nejaky label
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)



# Import pandas and cars.csv
cars = pd.read_csv('cars.csv',sep = ';', index_col= 0)

# Print out country column as Pandas Series
ps = cars['cars_per_cap']
print(ps)

# Print out country column as Pandas DataFrame
pdf = cars[['cars_per_cap']]
print(pdf)

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

# Print out first 4 observations
print(cars[0:4])

# Print out fifth, sixth, and seventh observation
print(cars[4:6])


#You can also use loc and iloc to perform just about any data selection operation.
# loc is label-based, which means that you have to specify rows and columns based on their row and column labels.
# iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

# Print out observation for Japan
print(cars.iloc[2]) # prints third row - numbering starts from 0

# Print out observations for Australia and Egypt
print(cars.loc[['USA', 'SK']]) # museli by byt v indexu


from tkinter import *


