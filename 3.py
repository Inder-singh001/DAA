import random
import time

print("Inderpreet Singh")
print("2104118")
print("\n")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def generate_random_roll_numbers(count):
    return [random.randint(1, 50) for _ in range(count)]


 # Generate a list of random roll numbers
roll_numbers = generate_random_roll_numbers(50)

# Measure the time taken to sort using quick sort
start_time = time.time()
quick_sort(roll_numbers)
end_time = time.time()
execution_time = end_time - start_time

print("Sorted Roll Numbers:", roll_numbers)
print(f"Time taken to sort: {execution_time:.10f} seconds")
