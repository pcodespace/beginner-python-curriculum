# Problem 1
# Count and print how many times "dog" appears in the list.
pets = ["dog", "cat", "dog", "hamster", "dog", "parrot"]
print(pets)
num_dogs = pets.count("dog")
print("There are", num_dogs, "dogs")


# Problem 2
# Count and print how many numbers are odd in the list (a number is odd if it's not divisible by 2).
numbers = [8, 3, 12, 7, 4, 11]
counter = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item % 2 != 0:
        counyer = counter + 1
print(counter, "odd numbers")





# Problem 3
# Search for "monkey" in the list and print its index if it's found.
animals = ["monkey", "elephant", "lion", "giraffe", "zebra"]
print(animals)
found = False
index = -1
for i in range (len(animals)):
    if animals[i] == "monkey":
        found = True
        index = 1
        break

if found == True:
    print("Found monkey at", index)
else:
    print("No monkeys in the list.")



# Problem 4
# Search for 99 in the list and print if it’s found.
numbers = [10, 45, 32, 99, 60, 5]
if 99 in numbers:
    print("Found 99.")
else:
    print("99 not found.")



# Problem 5
# Count and print how many numbers are even in the list (a number is odd if it's divisible by 2).
numbers = [13, 22, 8, 19, 6, 7]
counter = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 10:
        counter = counter + 1
print(counter, "numbers that are even")