import numpy as np

temperatures = np.array([12, 18, 22, 27, 16, 25, 29, 20, 17, 26])
print(temperatures[(temperatures < 18) | (temperatures > 25)])
