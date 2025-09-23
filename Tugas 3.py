set_A = {20, 30, 40, 50, 60}
set_B = {25, 30, 35, 40, 45}
set_C = {30, 40, 50, 70, 80}
set_D = {40, 50, 60, 90, 100}

O1 = set_A & set_C & set_D
print(O1)

O2_1 = set_A | set_B
O2_2 = O2_1.difference(set_D)
print(O2_2)

O3 = set_B ^ set_C
print(O3)

O4_1 = set_A | set_B
O4_2 = set_C | set_D
O4 = O4_1 & O4_2
print(O4)