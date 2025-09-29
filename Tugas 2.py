stok_buku={
    'harry potter':10,
    'laskar pelangi':15,
    'bumi manusia':7,
    'dilan 1990':20
}
print('buku:', list(stok_buku.keys()),'-stok:', list(stok_buku.values()))
key = input("Masukkan judul buku: ")
value = int(input("masukkan stok: "))
stok_buku[key] = value
print('buku', key, 'berhasil ditambahkan dengan stok', stok_buku[key])
print(stok_buku)