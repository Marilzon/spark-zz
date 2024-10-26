import time
import numpy as np
"""
processing range of values using native python3
"""
size = 10000

arr_x = np.arange(size)
arr_y = np.arange(size)

start = time.time()
result = arr_x + arr_y
end = time.time()

print(f"vct processing time {end - start:.4f} seconds")
