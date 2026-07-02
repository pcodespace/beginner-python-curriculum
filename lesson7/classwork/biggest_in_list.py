nums = [1, 4, 7, -4, 5]
print(nums)

# You can use built- in Python functions to find the biggest and smallest items
biggest_item = max(nums)
smallest_item = min(nums)

print("The biggest item:", biggest_item)
print("The smallest item:", smallest_item)

print("Our algorithm: Biggest Item in the List--")

biggest = nums[0]  # Start by assuming the first item is the biggest
for i in range(len(nums)): # Go through each item in the list
    if nums[i] > biggest:  # If we find something bigger, update our guess
        biggest = nums[i]
print("The biggest item:", biggest)

print("Our algorithm: Smallest Item in the List--")

smallest = nums[0]
for i in range(len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
print("The smallest item:", smallest)