# Problem 1
# Ask the user for their age.
# Calculate and print how many decades old they are, rounded to the nearest whole number.
#print("What is your age?")
age=float(input("Enter your age:"))
print("Your age is",age)
print("Your rounded age is", age//1)

# Problem 2
# Ask the user to enter a number.
# Print the result of multiplying that number by 5.
num=float(input("Enter your number:"))
print("5 times your number", num*5)

# Problem 3
# Use a for loop to print "I will learn Python!" 3 times.
#str1="I will learn Python!"
for i in range(1,4):
  print(f"I will learn Python!")


# Problem 4
# Ask the user for their name and age.
# Print their name and how old they will be one year in a single sentence.
username1=str(input("Enter your name:"))
print("Your name and your age",username1,age)

# Problem 5
# Use a for loop to print the numbers from 2 to 8, one per line.
for a in range(2,9):
     print("a",a)