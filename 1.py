print("Inderpreet Singh")
print("2104118")
print("\n")


def binary_search(roll_numbers, target):
    left, right = 0, len(roll_numbers) - 1

    while left <= right:
        mid = left + (left + right) // 2
        if roll_numbers[mid] == target:
            return mid  # Found the roll number
        elif roll_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Roll number not found

# college database sorted by roll numbers
roll_numbers = [101, 202, 303, 404, 505, 606, 707, 808, 909]

# Input roll number to search for
target_roll_number = int(input("Enter the roll no.: "))

print("Roll numbers in database: ", roll_numbers)
# Perform binary search
result = binary_search(roll_numbers, target_roll_number)

if result != -1:
    print(f"Roll number {target_roll_number} found at index {result}.")
else:
    print(f"Roll number {target_roll_number} not found in the database.")
