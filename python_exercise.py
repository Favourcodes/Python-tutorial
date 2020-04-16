house_price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * house_price
else: 
     down_payment = 0.2 * house_price
print(f"Down payment: ${down_payment}")

#importing libraries
import math
from math import factorial
math.factorial (5)

#Trying out comparison operators
#A sample of comparing the length of names
name_length = "M"
if len(name_length) < 3:  #The "len" shows the length of characters in a string
    print("name must be at least 3 characters ")
elif len(name_length) >50:
    print("name can be a maximum of 50 characters ")
else:
    print("name looks good! ")

#Weight converter
weight = int(input ("Weight: "))  #"int" coverts the user's input to integer and stores it in weight variable
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

#A Guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry you failed!")

#Car game
command = "" 
started = False
while command != "quit":
    command = input("> ").lower() #the "lower" function after the input is put there so that there will be no repetition of lower function after the command and it will help to store the input in lower case
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
        print("Car started...")
    
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
        print("Car stopped...")
    elif command == "help":
            print("""
start - to start the car
stop - to stop the car
quit - to quit
            """)
    elif command == "quit":
            break
    else:
        print("Sorry, I don't understand that")
        
