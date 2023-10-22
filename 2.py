import random
import time

print("Inderpreet Singh")
print("2104118")
print("\n")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def generate_random_roll_numbers(count):
    return [random.randint(1, 50) for _ in range(count)]


 # Generate a list of random roll numbers
roll_numbers = generate_random_roll_numbers(50)

# Measure the time taken to sort using merge sort
start_time = time.time()
merge_sort(roll_numbers)
end_time = time.time()
execution_time = end_time - start_time

print("Sorted Roll Numbers:", roll_numbers)
print(f"Time taken to sort: {execution_time:.10f} seconds")
