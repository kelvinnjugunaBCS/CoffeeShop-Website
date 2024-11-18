import random
import time

# Quickselect implementation to find the k-th smallest element
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

# Helper function to measure time for different values of N
def measure_runtime():
    ns = [100, 1000, 5000, 10000, 50000, 100000]  # Different N values
    runtimes = []

    for n in ns:
        arr = [random.randint(1, 1000000) for _ in range(n)]
        k = n // 2  # We are looking for the median

        start_time = time.time()
        quickselect(arr, k)
        end_time = time.time()

        runtimes.append(end_time - start_time)

    # Print the table
    print(f"{'N':<10}{'Time (seconds)':<20}")
    print("-" * 30)
    for i, n in enumerate(ns):
        print(f"{n:<10}{runtimes[i]:<20.6f}")

# Run the measurement
measure_runtime()
