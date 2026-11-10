import numpy as np

a = np.array([12, 25, 38, 41, 56, 63, 74, 82, 91, 100])
average = np.mean(a)
print("Среднее:", average)
print("Ниже среднего:", a[a < average])
