  # proses_buku.py
def hitung_total_halaman(daftar_halaman):
    return sum(daftar_halaman)
def rata_rata_halaman(daftar_halaman):
    return sum(daftar_halaman) / len(daftar_halaman)
def buku_terbanyak(daftar_buku, daftar_halaman):
    max_halaman = max(daftar_halaman)
    index = daftar_halaman.index(max_halaman)
    return daftar_buku[index], max_halaman
