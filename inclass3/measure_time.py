"""
measure_time.py
Measures the elapsed time for calculating the 1 million's power of 1 million
Kyle Ponte
kponte@stevens.edu
9/24/25
"""

import math
import time

start_time = time.time()
math.pow(1000000,1000000)
end_time = time.time()
print(f"The elapsed time was {end_time - start_time} seconds")