animals = ["Aardvark", "Cat", "Aardvark", "Cat", "Dog"]
print(animals)

# You can use built-in Python functions to count some items.
num_cats = animals.count("Cat")
print("There are", num_cats, "Cats.")

print("Our algorithm:")

counter = 0
for i in range(len(animals)):   # Go through each item in the list.
    item = animals[i]
    if item == "Cat": # Check if the item is "Cat" 
        counter = counter + 1 # If the item is "Cat", add 1 to the counter
print(counter,"Cats")

numbers = [14, 1, 50, 4, 20, 12,89,67]
print(numbers)
counter = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 10:
        counter = counter + 1
print(counter, "numbers above 10")