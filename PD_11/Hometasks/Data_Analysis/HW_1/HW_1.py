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

# x = np.array([
# [20.1, 20.3, 19.8],
# [21.0, 20.7, 20.2],
# [19.5, 19.8, 19.3],
# [20.8, 21.1, 20.6]
# ])
#
# print(np.average(x, axis = 0))
# print(np.sum(x, axis = 1))
# print(np.var(x, axis = 0, ddof = 1))
# print(np.argmin(np.var(x, axis = 0, ddof = 1)))

# Задание № 4:

# x = np.array([
# [20.1, 20.3, 19.8],
# [21.0, 20.7, 20.2],
# [19.5, 19.8, 19.3],
# [20.8, 21.1, 20.6]
# ])
#
# col_min = np.min(x, axis = 0)
# col_max = np.max(x, axis = 0)
# col_range = col_max - col_min
# x = np.array((x - col_min)/col_range)
#
# print("col_mins:\n", col_min, "\n", "col_maxs:\n", col_max)
# print("col_range:\n", col_range)
# print("x:\n", x)
# print(np.sum(x, axis = 0))

# Задание № 5:

# ph = np.array([
# [7.1, 7.4, 7.0],
# [6.9, 7.2, 7.1],
# [7.3, 7.5, 7.2],
# [7.0, 7.1, 6.8],
# [6.8, 6.9, 6.7],
# [7.4, 7.6, 7.3]
# ])
#
# print("averages:\n", np.average(ph, axis=1))
# print("sums:\n", np.sum(ph, axis = 0))
# print("total_sums:\n", np.sum(ph, axis = 1))
# print("var:\n", np.var(ph, axis = 0, ddof = 1))

