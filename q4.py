import numpy as np
A = np.random.rand(10,1)

print(A)

def func(x):
    return (1 / (1 + np.exp(-x)))
result = np.apply_along_axis(func, 0, A)
print(result)