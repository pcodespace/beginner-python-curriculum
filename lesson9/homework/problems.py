# Problem 1
# Use a while loop to print the word "Python" 4 times.
print("--------------------------Problem 1-----------------------------------")
for i in range(4):
    print("Python")

# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
print("--------------------------Problem 2-----------------------------------")
i = 2
while i < 13:
    print(i)
    i = i + 2




# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.
print("--------------------------Problem 3-----------------------------------")
num = int(input("Enter a positive number:"))
i = 0
while i < num + 1:
    print(i)
    i = i + 1


# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.
print("--------------------------Problem 4-----------------------------------")
number = int(input("Enter a number greater than 10: "))
i = number
while i > 0:
    print(i)
    i = i - 5


# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
print("--------------------------Problem 5-----------------------------------")
animals = ["cat", "rat", "mouse"]
print(animals)
i = 0
while i < 3:
    print(animals[i],  "is awesome!")
    i = i + 1