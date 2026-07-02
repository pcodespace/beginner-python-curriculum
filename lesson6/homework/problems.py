# Problem 1
# Count and print how many times "Alex" appears in the list.
print("---------------------Problem 1-------------------")
names = ["Liam", "Alex", "Sophie", "Alex", "Mia","Alex"]
print(names)
num_names = names.count("Alex")
print("There are", num_names, "Alex.")

# My count algorithm
counter_names=0
for i in range(len(names)):
  item=names[i]
  if item == "Alex": #check if item_names is Alex
     counter_names = counter_names+1
print("Using Algorithm There are ", counter_names, "Alex.")


# Problem 2
# Search for "elephant" in the list and print if it's found.
print("---------------------Problem 2-------------------")
animals = ["zebra", "giraffe", "lion", "tiger", "elephant"]
print(animals)
if "elephant" in animals:
    print("Found elephant.")
else:
    print("No elephants found.")

  #My algorithm
found = False
indexOne = -1

for i in range (len(animals)):
  if animals[i] == "elephant":
      found = True
      indexOne= i + 1
      break
if found == True:
    print("Found elephant in the list using Algorithm:")
else:
    print("No elephants in the list using Algorithm:")
   


# Problem 3
# Count and print how many scores are 100.
print("---------------------Problem 3-------------------")
scores = [95, 100, 88, 100, 77, 92, 100]
print(scores)
counter = 0
for i in range(len(scores)):
    item = scores[i]
    if item == 100:
        counter = counter + 1
print(counter, "scores equal to 100")


# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
print("---------------------Problem 4-------------------")
colors = ["red", "green", "blue", "yellow"]
print(colors)
for i in range (len(colors)):
    if colors[i] == "blue":
        found = True
        index = i+1
        break

if found == True:
    print("Found blue at", index)
else:
    print("No blue in the list.")


# Problem 5
# Count and print how many temperatures in the list are below zero.
print("---------------------Problem 5-------------------")
temperatures = [3, -2, 5, -7, 0, 4, -1]
print(temperatures)
counter = 0
for i in range(len(temperatures)):
    item = temperatures[i]
    if item < 0:
        counter = counter + 1
print(counter, "temperatures below 0")