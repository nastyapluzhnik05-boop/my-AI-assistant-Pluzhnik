import numpy as np

scores = np.array([
    [65, 42, 78, 90],
    [88, 56, 95, 82],
    [51, 89, 34, 27]
])

mean_scores = np.mean(scores, axis=1)
print(mean_scores)
max_scores = np.max(mean_scores)
print(max_scores)
