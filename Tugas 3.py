print("Masukkan nilai atau ketik spasi jika sudah selesai memasukkan nilai")

total = 0
count = 0

while True:
    nilai = input("Masukkan nilai : ")
    if nilai == ' ':
        break
    try:
        number = int(nilai)
        total += number
        count += 1
    except ValueError:
        print("Input salah pastikan anda memasukkan angka yang benar.")

if count > 0:
    average = total / count
    print("Rata rata:", average)