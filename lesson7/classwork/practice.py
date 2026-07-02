# Problem 1
# Find and print the total sum of all the numbers in the list.
print("------------------------------------------------------------------------------")
numbers = [4, 11, 22, -6, 3, -9, 1]
print(numbers)
total = sum(numbers)
print("Our algorithm:")
total = 0
for i in range(len(numbers)):
    item = numbers[i]
    total = total + item
print("The sum is:", total)
print("---------------------------------------------")

# Problem 2
# Find and print the biggest number in the list.
numbers2 = [-9, 17, 5, -3, 0, -31, 67]
print(numbers2)
biggest_item = max(numbers2)
smallest_item = min(numbers2)
print("Our algorithm:")
biggest = numbers2[0]  # Start by assuming the first item is the biggest
for i in range(len(numbers2)): # Go through each item in the list
    if numbers2[i] > biggest:  # If we find something bigger, update our guess
        biggest = numbers2[i]
print("The biggest item:", biggest)
print("------------------------------------------")




# Problem 3
# Find and print the sum of only the negative numbers in the list (negative means less than 0).
numbers3 = [2, -1, 8, 10, -7, 6]
print(numbers3)
total2 = 0
for i in range(len(numbers3)):
    item = numbers3[i]
    if item < 0:
        total2 = total2 + item
print("The sum of only the negative numbers is:", total2)
print("-------------------------------")

# Problem 4
# Find and print the sum of only the even numbers in the list. 
numbers4 = [8, 3, 15, 22, 11, 6]
print(numbers4)
total3 = 0
for i in range(len(numbers4)):
    item = numbers4[i]
    if item % 2 == 0:
        total3 = total3 + item
print("The sum of the even numbers in the list is:", total3)
print("------------------------------")
      


# Problem 5
# Find and print the biggest number that is negative in the list.
# The biggest number that is negative in the list means it is the smallest number in the list
numbers5 = [-1, -30, -5, 7, 12, -2]
print(numbers5)
smallest = numbers5[i]
for i in range(len(numbers5)):
    item = numbers5[i]
    if item < smallest and item < 0:
        smallest = item
print("Biggest negative number is:", smallest)       