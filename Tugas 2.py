identity_matrix = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
print(identity_matrix)

x = int(input("masukkan ukuran matrix:"))

matrix2 = [[1 if i == j else 0 for j in range(x)] for i in range(x)]
print(matrix2)