#input_buku.py

def input_petugas():
    nama = input("Masukkan nama petugas: ")
    return nama


def input_buku():
    daftar_buku = []
    daftar_halaman = []

    for i in range(3):
        print(f"\nBuku ke-{i+1}")
        judul = input("Judul buku: ")

        # Validasi supaya input angka
        while True:
            try:
                halaman = int(input("Jumlah halaman: "))
                break
            except ValueError:
                print("Harus berupa angka!")

        daftar_buku.append(judul)
        daftar_halaman.append(halaman)

    return daftar_buku, daftar_halaman
