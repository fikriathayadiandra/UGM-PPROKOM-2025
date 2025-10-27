import numpy as np
A = np.array([
 [2, 4, 6],
 [1, 3, 5]
])
B = np.array([
 [1, 1, 1],
 [2, 2, 2]
])

print("penjumlahan :", A + B)
print("pengurangan :", A - B)
C = B.transpose()
print("A.B(transpose) :", A.dot(C))