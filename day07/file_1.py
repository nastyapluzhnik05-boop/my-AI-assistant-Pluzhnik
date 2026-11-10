import numpy as np

data = np.array([
    [23, 42, 67, 80],
    [98, 53, 75, 89],
    [19, 34, 56, 78],
    [45, 67, 89, 90]
])

new_data = data.copy()
new_data[new_data < 60] = new_data[new_data < 60] + 10
print(new_data)


 






