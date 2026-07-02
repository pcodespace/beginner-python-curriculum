# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
print("-------------------Problem 1------------------------------")
print(numbers)
total = 0
for i in range(len(numbers)):
    if numbers[i] > 25:
        total = total+numbers[i]
print("The sum of all the numbers greater than 25 is:", total)

# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
numbers2 = [-5, -20, -11, 0, 4, -15]
print("---------------Problem 2----------------------")
print(numbers2)
total2 = 0
for i in range(len(numbers2)):
    if numbers2[i] < -10:
        total2 = total2 + numbers2[i]
print("The sum of the numbers less than -10 is:", total2)


# Problem 3
# Find and print the biggest number less than 100 in the list.
numbers3 = [104, 99, 86, 120, 101]
print("--------------Problem 3----------------------")
print(numbers3)
biggest = 0
for i in range(len(numbers3)):
    if numbers3[i] < 100 and biggest < numbers3[i]:
        biggest = numbers3[i]
print("The biggest number which is less than 100 in the list is:", biggest)



# Problem 4
# Find and print the biggest number in the list.
numbers4 = [12, 7, 33, 5]
print("--------------------Problem 4----------------------------")
print(numbers4)
biggest2 = 0
for i in range(len(numbers4)):
    if numbers4[i] > biggest2:
        biggest2 = numbers4[i]
print("The biggest number in the list is:", biggest2)


# Problem 5
# Find and print the total sum of all the numbers in the list.
numbers5 = [1, 3, 5, 7, 9]
print("----------------Problem 5-------------------------")
print(numbers5)
total3 = 0
for i in range (len(numbers5)):
    item = numbers5[i]
    total3 = total3 + item
print("The sum is:", total3)