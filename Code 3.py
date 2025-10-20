from array import array
x1 = int(input("masukkan angka pertama: "))
x2 = int(input("masukkan angka kedua: "))
x3 = int(input("masukkan angka ketiga: "))
x4 = int(input("masukkan angka keempat: "))
x5 = int(input("masukkan angka kelima: "))
arr_nilai = array('i', [x1, x2, x3, x4, x5])
print(arr_nilai, "Jumlah elemen array :", len(arr_nilai))
print("nilai rata rata elemen:", (x1+x2+x3+x4+x5)//len(arr_nilai))