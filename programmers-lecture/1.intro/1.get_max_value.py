import time

n = int(input("The number of elements: "))
haystack = [k for k in range(n)]

print("Searching for the maximum value...")

ts = time.time()
maximum_value = max(haystack)
elapsed = time.time() - ts

print("Maximum element = %d, Elaspsed time = %.2f" % (maximum_value, elapsed))
