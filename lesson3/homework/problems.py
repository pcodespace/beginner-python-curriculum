import random
# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
user_num6=int(input("Enter your number:"))
if user_num6 %2==0:
    print("Your number is even.",user_num6)
else:
    print("Your number is odd.",user_num6)


# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
user_str1=input(("Enter a day of the week."))
if user_str1=={"monday", "tuesday", "wednesday", "thursday", "friday"}:
    print("Weekday",user_str1)
else:
    if user_str1==("saturday", "sunday"):
        print("Weekend",user_str1)
    

# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
num=random.randint(1,10)
user_num4=int(input("Guess the random number from 1 to 10:",))
if user_num4==num:
    print("Correct!")
else:
    print("Try again.")


# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
user_num3=int(input("Enter a postive integer:"))
if user_num3 >10 and user_num3 %2==0:
    print("Big even number.",user_num3)
else:
    print("Number does'nt meet criteria of Big Even Number.",user_num3)    




# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
user_num1=int(input("Enter number 1:"))
user_num2=int(input("Enter number 2:"))
if user_num1 > user_num2:
    print("Your first number is greater than your second number.",user_num1)
elif user_num1 == user_num2 :
    print("Your numbers are equal.")
elif user_num1<user_num2:
    print("Your first number is less than your second number.")     

