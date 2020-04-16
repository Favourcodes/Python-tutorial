#print(f"Hello, world! This is my first attempt")
#print(" o----")
#print("   ||||")
#print("*" * 10)
#price = 10
#price = 20
#rating = 4.6
#name = "Mosh"
#is_published = False
#print(price)

#To print a patient's name, age and show if he/she is a new patient or not
patient_name='John Smith'
print (patient_name)
age = 20
print(age)
new_patient='True'
print(new_patient)

#To receive input from a user
name = input("What is your name? ")
print("Hi " + name)

#Exercise on color
name = input("what is your name and favorite color? ")
favorite_color = input("What is your favourite color? ")
print(name + " likes " + favorite_color)

#To calculate the age of someone
birth_year = input("Birth year")

#To print the type of birth year
print(type(birth_year))
age = 2020 - int (birth_year)

#To print the type of age
print(type(age))
print(age)

#To print the weight of a user and convert from pounds to kilogrammes
weight_lbs = input("Weight (lbs): ")
weight_kg = int (weight_lbs) * 0.45
print(weight_kg)

#To get a multi line string
course = '''
Hi John,

Here is our first email to you.

Thank you,
The support team
'''
print (course)

#To get the index of a character
course = 'Python for beginners'
print(course[-2])

#To see multiple indexes
course = 'Python for beginners'
print(course[0:3])

#formatted strings
first = 'John'
last = 'Smith'
message = f"{first} [{last}] is a coder"
print(message)

#String method
course = 'python for beginners'
print(len(course)) #The "len" functions shows the length of characters
 
#To print a message in upppercase you use ".upper" function
course = "Python for Beginners"
print(course.upper())
print(course.lower())#To print a message in lower cases

#Arithmetic precedence
#In Python, BODMAS is used to solve arithmetic problems
#THis is the order of aruthmetic execution: exponentiation (e.g 2**3), multiplication or division, addition or subtraction
x = 10 + 3 * 2
print(x)

#Arithmetic function
x = 3.9
print(round(3.9))

#if statement
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")

    #To terminate the indent press shift and tab together

elif is_cold: # 'elif' is the built in syntax of 'else if' in python
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print ("It's a lopvely day")
print("Enjoy your day")

#Logical operators
#AND: both should be true
#OR: at least one conditon should be true
#"AND" sample
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

#"OR" sample
has_high_income = True
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")

#NOT operator
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

#importing libraries
import math
n = 3
k = 5
math.factorial(6)/ (math.factorial(k) * math.factorial(n - k))
