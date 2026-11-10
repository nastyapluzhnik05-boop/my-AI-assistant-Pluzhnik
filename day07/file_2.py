import numpy as np

numbers = np.arange(1, 17)
table = numbers.reshape(4, 4)
print(table)
print(table[1:3, 1:3])
