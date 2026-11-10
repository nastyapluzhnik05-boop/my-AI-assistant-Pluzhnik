import numpy as np

numbers = np.array([34, 90, 67, 23, 42, 67, 89, 84])
average = np.mean(numbers)
below = numbers[numbers < average]
print(average)
print(below)