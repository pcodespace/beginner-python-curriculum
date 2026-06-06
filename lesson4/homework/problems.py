# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
user_test1=int(input("What is your first test score?:"))
user_test2=int(input("What is your second test score?:"))
if user_test1>=50 and user_test2>=50:
    print("You passed BOTH tests!")
else:
    print("You failed at least one. Fix the errors on your tests.")
print("Test Score check complete")


# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
user_lunch=input("Did you bring your lunch for your picnic? (yes/no)")
user_water=input("Did you bring your water for your picnic?(yes/no)")
if user_lunch=="yes" and user_water=="yes":
    print("You're fully ready for your picnic!")
elif user_lunch=="yes" and user_water=="no":
    print("You're somewhat ready for your picnic.")
elif  user_lunch=="no" and user_water=="yes":
    print("You're somewhat ready for your picnic.")
else:
    print("You are not ready for your picnic.")
print("Lunch and water check complete")

# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
user_num3=int(input("Enter a number.:"))
if  user_num3==0 or user_num3==1 or user_num3==2 or user_num3==3 or user_num3==4 or user_num3==5 or user_num3==6 or user_num3==7 or user_num3==8 or user_num3==9 or user_num3==10:
    print("In range,between [1-10]")
else:
    print("Out of range.")
print("Number Range check complete.")


# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
num1=random.randint(1,10)
user_num4=int(input("Guess your number:"))
if num1==user_num4 and num1%2==0:
    print("Even match!")
elif num1==user_num4 or num1==5:
    print("Nice try!")
else:
    print("Nope.")
print("Problem 4,Random number check complete.")

# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
user_num1=int(input("Enter your first number:"))
user_num2=int(input("Enter your second number:"))
if user_num1%5==0 and  not user_num2 %2==0:
    print("Interesting pair!")
elif not user_num1%2==0 and user_num2%5==0:
    print("Interesting pair!")
else:
    print("Plain pair!")
print("Problem 5 check complete.")

