# Problem 1
# Write a function that returns the number 42 and print the result = num
print("---------------------Problem 1-----------------------------------")
def build_number():
    number = "42"
    return number
num = build_number()
print("The number is", num)

# Problem 2
# Write a function that returns "penguin" and print the result.
print("---------------------Problem 2-----------------------------------")
def make_animal():
    animal = "penguin"
    return animal
bird = make_animal()
print("The animal is", bird)


# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.
print("---------------------Problem 3-----------------------------------")
fruit = "guava"
def show_fruit():
    print("The fruit is", fruit)

show_fruit()

def modify_fruit():
    global fruit
    fruit = "banana"

modify_fruit()
show_fruit()


# Problem 4
# Write a function that takes two parameters: first_name and last_name.
# The function should return a string that combines the first and last names separated by a space.
print("---------------------Problem 4-----------------------------------")
def make_full_name(first_name, last_name):
    return first_name + " " + last_name
full_name = make_full_name("Mary", "Brooks")
print(full_name)


# Problem 5
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).
print("---------------------Problem 5-----------------------------------")
def calculate_perimeter(length, width):
    return 2 * (length + width)
print("The perimeter of a 5x3 rectangle is:", calculate_perimeter(5, 3))