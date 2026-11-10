for x in range(5):
    print(x)
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Привет")

import numpy as np

a = np.array([10, 20, 30])
print(a[0])
print(np.mean(a))
