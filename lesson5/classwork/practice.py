import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.

car_brands = ["Acura", "BMW", "GMC", "Honda"]
print("First car:", car_brands[0])
print("Last car:", car_brands[3])
                            
car_brands.append("GMC")
print(car_brands)

# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.

numbers = [1, 6, 4, 3, 2]
print(numbers[2])
numbers.insert(2,921)
print(numbers)

# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then remove one city and print the updated list.
cities=["Bellevue", "Bothell", "Clyde Hill"]
length = len(cities)
last_city = len(cities) - 1
print(cities[last_city])


# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
# Hint: The word pop also means removing something.
import random

file_extensions=["container tools", "markdownlint", "pylance", "python", "python debugger", "python enviornments"]
random_extension = random.choice(file_extensions)
print(random_extension)

# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then count how many times a specific name appears.
name_list=["Adam", "Dennis", "Ben", "Luke", "Peter", "Lily", "Salma", "Max"]
last_name = len(name_list)-1
middle_name=int(last_name/2)
print("The name in the middle is:",name_list[middle_name])
