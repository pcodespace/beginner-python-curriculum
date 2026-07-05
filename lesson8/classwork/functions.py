# Definte a function that returns a greeting
def make_greeting():
    greeting = "Hello, world!"
    return greeting  # Sends the greeting back to where the function was called

message = make_greeting()  # Call the make_greeting() function
print(message)

# Define a function that makes a face
def build_face():
    face = ":)"
    return face  # Sends the face back to where the function was called.

person = build_face()  # Call the build_face() function.
print("Here is our person", person)

# Parameters are local variables that can be only accessed inside a function

# Define a function that returns a personalized greeting based on name
def personalized_greeting(name): # name is a parameter
    greeting = "Hello, " + name + "!"
    return greeting # Sends the greeting back to where the function was called

personalized_message = personalized_greeting("Benjamin")
print(personalized_message)

# Define a function that returns the area of a rectangle based on length and width
def calculate_rectangle_area(length, width):  # Length and width are parameters.
    area = length * width
    return area

print("The area of a 5x3 rectangle is:", calculate_rectangle_area(5, 3))