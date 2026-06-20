colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]  #created a list

print(colors)  #print the whole list

# Lists are 0 indexed
print("First color:", colors[0])  #accessed items in a list by index
print("Second color:", colors[1])
print("Third color:", colors[2])
print("Fourth color:", colors[3])
print("Fifth color:", colors[4])
print("Sixth color:", colors[5])

# Error: list index out of range
# print(colors[10])

colors.append("Orange") # Add an item at a specific index
print("After append:", colors)

colors.insert(2, "purple") # Add an item at a specific index
print("After insert:", colors)

colors.remove("green") # Remove the first occurence of an item
print("After removing 'green':", colors)
      
index_of_blue=colors.index("blue") # Find the index of an item
print("Index of 'blue:", index_of_blue)

colors.append("blue")
blue_count = colors.count("blue")

print("Count of 'blue':", blue_count)

colors.sort()  # Sort the list in alphabetical order
print("After sort:", colors)

colors.reverse()    # Reverse the order of the list
print("After reverse:", colors)