import numpy as np
test_matrix = np.array([
    [3, 0],
    [1, 2]
])

print(test_matrix)
print(test_matrix[0][1])
print(test_matrix[1][1])

print("------------------")
test_eig, test_v = np.linalg.eig(test_matrix)
print(test_eig)
print(test_v)