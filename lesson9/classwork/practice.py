# Problem 1
# Use a while loop to print the numbers from 1 to 7 (inclusive).
print("----------------------------------Problem 1--------------------------------------------------------")
i = 1
while i < 8:
    print("The numbers from 1 to 7:", i)
    i = i + 1



# Problem 2
# Use a while loop to count down from 3 to -3 (inclusive), printing each number.
print("----------------------------------Problem 2--------------------------------------------------------")
i2 = 3
while i2 > -4:
    print(i2)
    i2 = i2 - 1


# Problem 3
# Ask the user to input a number less than 50.
# Use a while loop to print numbers starting from that number, going up by 2 each time, until you reach 50 (inclusive).
print("----------------------------------Problem 3--------------------------------------------------------")
number = int(input("Enter a number less than 50:"))
i3 = number
while i3 < 51:
    print(i3)
    i3 = i3 + 2


# Problem 4
# Ask the user to input a number.
# Use a while loop to count down by 3 each time until you reach 0 or less (inclusive).
print("----------------------------------Problem 4--------------------------------------------------------")
i = int(input("Enter a number: "))
while i >= 0:
    print(i)
    i = i - 3 


# Problem 5
# Use a while loop to print each element in the list.
print("----------------------------------Problem 5--------------------------------------------------------")
items = ["chair", "table", "desk"]

i5 = 0
while i5 < len(items):
    print(items[i5])
    i5 = i5 + 1

# Problem 6
# Ask the user to enter a positive integer.
# Use a while loop to reverse the digits of the number.
# Print the reversed number.
print("----------------------------------Problem 6--------------------------------------------------------")
num = int(input("Enter your positive number: "))
reversed_number = 0
while num > 0:
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num = num // 10

print(reversed_number)