# Problem 1
# Ask for age and height.
# If age is at least 10 AND height is at least 120 cm, print "You can ride!"
# Otherwise, print "Sorry, you can't ride."

age=int(input("What is your age if you want to ride the roller coaster?"))
height=int(input("What is your height in cm?"))

if age >=10 and height >= 120:
    print("You can ride the roller coaster.")
else:
    print("Sorry, you can't ride.")

# Problem 2
# Generate a random number between 1 and 5.
# Ask the user to guess.
# If they guessed right OR the number is 3, print "Lucky!"
# Otherwise, print "Not today."


import random
num = random.randint(1,5)
user_num = int(input("Give me a number from 1 to 5:"))
if user_num == num or num ==3:
    print("Lucky!")
else:
    print("Not today.")

# Problem 3
# Ask the user to enter 3 numbers.
# If NOT all of them are even (meaning at least one is odd), print "Odd one detected!"
# Otherwise, print "All even!"

a= int(input("Give me a number."))
b= int(input("Give me a number."))
c= int(input("Give me a number."))

if not (a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
    print("Odd one detected!")
else:
    print("All EVEN!")
# Problem 4
# Ask if the user has a membership and if they scored 100 points in a game.
# If they have a membership OR scored 100, print "You earned a bonus pass!"
# Otherwise, print "No bonus pass."


has_membership = input("Do you have a membership?(yes/no)")
score=int(input("What is your score in the game?"))

if has_membership == "yes" or score == 100:
    print("You scored a BONUS PASS!")
else:
    print("No bonus pass.")

# Problem 5
# Ask the user for a number.
# If it's divisible by 3 AND (either less than 0 OR greater than 100), print "Weird number!"
# Otherwise, print "Normal number."
user_num1=int(input("Give me a number:"))
if user_num1 <0 or user_num1 >100 and user_num1 %3==0:
    print("WEIRD NUMBER!")
else:
    print("Normal number.")