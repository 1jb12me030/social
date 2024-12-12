list1 = [1, 2, 3, 4, 5, 6, 77, 22, 33, 44]

# Initialize the highest and second highest variables
highest = second_highest = float('-inf')

# Loop through each number in the list
for number in list1:
    # Update highest and second highest accordingly
    if number > highest:
        second_highest = highest  # Update second highest
        highest = number  # Update highest
    elif number > second_highest and number != highest:
        second_highest = number  # Update second highest

# Output the results
print("Highest number:", highest)
print("Second highest number:", second_highest)