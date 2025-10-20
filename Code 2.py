nama1 = input(str("masukkan nama 1: "))
nama2 = input(str("masukkan nama 2: "))
nama3 = input(str("masukkan nama 3: "))
nama4 = input(str("masukkan nama 4: "))
nama5 = input(str("masukkan nama 5: "))
list_nama = [nama1, nama2, nama3, nama4, nama5]
print(list_nama)

g1 = int(input("ingin ganti nama pada indeks ke berapa? "))
namabaru = str(input("ingin ganti nama tersebut menjadi apa? "))
list_nama[g1] = namabaru
print(list_nama)