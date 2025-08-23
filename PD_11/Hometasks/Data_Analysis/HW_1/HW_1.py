import numpy as np

# Задание № 1:

# temps = np.array([15.2, 16.8, 14.5, 17.0, 16.1])
# print(temps.sum(), "\n", temps.mean(), "\n", temps.min(), "\n", temps.max())

# Задание № 2:

# h1 = np.array([45, 50, 47])
# h2 = np.array([48, 46, 52])
# print(np.sum([h1, h2], axis = 0))
# print(np.prod([h1, h2], axis = 0))

# Задание № 3:

x = np.array([
[20.1, 20.3, 19.8],
[21.0, 20.7, 20.2],
[19.5, 19.8, 19.3],
[20.8, 21.1, 20.6]
])

print(np.average(x, axis = 0))
print(np.sum(x, axis = 1))
print(np.var(x, axis = 0, ddof = 1))
print(np.argmin(np.var(x, axis = 0, ddof = 1)))