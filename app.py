'''
message = 'mustafa noor will be a coder'
print(message.upper())
print(message.lower())
print(message.replace('coder', 'excellent coder' ))
print(message.find("will"))
print("Mustafa" in message)

'''
'''
print(10+3)                             #ORDER PRECEDENCE
print(10-3)                             #FIRST PARENTHESIS, EXPONENTIATION, MULTIPLICATION OR DIVISION, THEN ADDITION OR SUBTRACTION
print(10*3)
print(10/3)
print(10//3)
print(10%3)
'''
'''
#PERFORMING CALCULATIONS

import math
print(math.floor(2.9))
print(math.ceil(2.9))
'''

#IF STATEMENTS
'''
payment = 1000000
buyer_good_credit = False
if buyer_good_credit:
    downpayment = 0.10 * 1000000
else:
    downpayment = 0.20 * 1000000

print( f"the customers down-payment is: ${downpayment}")
'''
'''
temperature = 34

if temperature >=35:
    print('It is a hot day')
else:
    print('This is normal ')
'''
'''
# another if statement question

name = input("please enter your name : ")

if len(name) <= 3 :
    print("Your name must be greater than 3 characters. ")
elif len(name) >= 50:
    print("Your name should not be greater than 50 characters. ")
else:
    print("Your name looks good. ")
'''
'''
# converting the weight into the kgs and vice versa

weight = int(input("Please enter your weight. And then select its units. "))
units = input("(kg) or (lbs) ")

if units == "kg" :
    new_weight = weight * 2.20
    print(f"weight is {new_weight} pounds")
else:
    new_weight = weight*0.45
    print(f"weight is {new_weight} kgs")
'''
'''
# while loop
i=1
while i<=5:
    print(i)
    i=i+1
print("done")
'''
'''
# Guess game: guess a number and see if its right in three tries

secret_number = 6
count = 0
guess_tries = 3
while count < guess_tries :
    guess = int(input("Guess?? : "))
    count += 1
    if guess == secret_number:
        print("You won!! ")
        break
else :
    print("Better luck next time :) ")
'''
'''
#car game

car_engine= ""
car_started = False
car_stopped = False
while True:
    car_engine = input("> ")
    if car_engine == "help" :
        print(" Start - To start the car \n Stop - To stop the engine \n Quit - To exit from the game")
    elif car_engine == "start":
        if car_started:
            print("The car is already started...")
        else:
            car_started = True
            print("Engine is on. ")
    elif car_engine == "stop":
        if car_stopped:
            print("Car is already stopped...")
        else:
            car_stopped = True
            print("Engine is off")
    elif car_engine == "quit":
        print(" The game has ended ... ")
        break
    else:
        print("Sorry system didn't understand")

'''
'''
# calculating the items in the shopping cart

prices = [10,20,30]
total_value = 0
for price in prices:
    total_value += price
print(f"Total: ${total_value}")
'''



















