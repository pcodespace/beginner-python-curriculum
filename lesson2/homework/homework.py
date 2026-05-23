# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
User_input1 = input("Enter the first number: ")
User_input2 = input("Enter the second number: ")

quotient = int(User_input1) // int(User_input2)
remainder = int(User_input1) % int(User_input2)

print(quotient)
print(remainder)

# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
user_animal = input("Enter your favorite animal: ")
user_color = input("Enter your favorite color: ")

print(f"A {user_color} {user_animal} would be awesome!")

# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).

for i in range(0, 11, 2):
    print(i)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
user_pushups = int(input("How many push-ups can you do? "))
print(f"In a week, you could do {user_pushups * 7} push-ups!")

# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for z in range(1,7):
   print(f"z and z squared=",z, z*z)