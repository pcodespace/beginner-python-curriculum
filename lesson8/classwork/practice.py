# Problem 1
# Write a function that returns your favorite fruit and print it.
def make_fruit():
    fruit = "Mango"
    return fruit
message = make_fruit()
print(message)


# Problem 2
# Write a function that returns a smiley face and print it.
def build_face():
    face = ":)"
    return face
person = build_face()
print("Here is our person", person)


# Problem 3
# Write a function that takes three parameters: length, width, and height.
# It should return the volume (length * width * height).
def calculate_cube_volume(length, width, height):
    volume = length * width * height
    return volume
print("The volume of a 3x3x3 cube is:", calculate_cube_volume(3, 3, 3))


# Problem 4
# Create a variable for a book, then print it.
# Modify it inside a function and print it again.
book = "City Spies"

def show_book():
    print("The book is", book)

show_book()

def modify_book():
    global book  # Before changing a global variable inside a function, you need to do this.
    book = "Holes"

modify_book()
show_book()


# Problem 5
# Write a function that takes one parameter num.
# The function should return the value of num multiplied by 2.
def multiply(num):
    return num * 2