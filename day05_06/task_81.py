import numpy as np

group1 = np.array([55, 84, 42, 72, 67, 98, 23, 89])
group2 = np.array([65, 74, 81, 59, 90, 77, 68, 85])

print("Группа 1: среднее", np.mean(group1), "зачётов", np.sum(group1 >= 60), "максимум", np.max(group1))
print("Группа 2: среднее", np.mean(group2), "зачётов", np.sum(group2 >= 60), "максимум", np.max(group2))
