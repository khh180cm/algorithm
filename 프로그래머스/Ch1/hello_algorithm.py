import time

n = int(input("Number of elements: "))
haystack = [i for i in range(n)]

ts = time.time()
maximum = max(haystack)
elapsed = time.time() - ts

print(f"Maximum element: {maximum}, Elapsed time: {elapsed:.2f}")
