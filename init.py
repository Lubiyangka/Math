from scipy import optimize
import numpy as np
minC = np.array([5, 10])
maxC = np.array([-i for i in minC])
A = np.array([[3, 2], [5, 10]])
B = np.array([1200, 10000])
bounds = [[114, None], [106, None]]
res = optimize.linprog(maxC, A, B, bounds=bounds)
print(res)



