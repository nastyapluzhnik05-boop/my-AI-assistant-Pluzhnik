import numpy as np

numbers = np.array([45,60,72,88,51,95,80,79])

needed = numbers[(numbers >=60) & (numbers <= 80)]
print(needed)