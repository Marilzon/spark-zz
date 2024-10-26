import time

"""
processing range of values using vectorized programming with numpy
"""
size = 10000

arr_x = range(size)
arr_y = range(size)

start = time.time()
result = [arr_x[i] + arr_y[i] for i in range(size)]
end = time.time()

print(f"ntv processing time {end - start:.4f} seconds")
