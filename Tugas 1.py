A = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
    ]
print("elemen pada lapisan pertama :", A[0])
hasil = []
for i in range(len(A)):
    for j in range(len(A[i])):
        print(f"lapisan {i} baris {j} -> {A[i][j][-1]}")
