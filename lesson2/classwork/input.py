user_input = input("Give me an integer: ")  #input ALWAYS returns a string
print(user_input)

#Error:cannot add an integer to a string
#print(user_input + 1)

number = int(user_input)
print(number + 1)