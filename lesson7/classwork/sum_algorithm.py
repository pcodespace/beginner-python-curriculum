nums = [5, -8, 35, -3, 6, 2]
print(nums)

total = sum(nums) # Shortcut to find the sum
print("The sum is:", total)

print("Our algorithm:")

total = 0
for i in range(len(nums)):  # Go through each index
    item = nums[i]  # Accessing the number at index i
    total = total + item  # Add the item to the running total
print("The sum is:", total)

# Find sum of only positive numbers
total = 0
for i in range(len(nums)):  # Go through each index
    item = nums[i]  # Accesing the number at index i
    if item >= 0:  # Positive means >= 0
        total = total + item
print("The sum of only the positive numbers is:", total)