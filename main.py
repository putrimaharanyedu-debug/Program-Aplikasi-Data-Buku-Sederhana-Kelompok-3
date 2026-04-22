from input_buku import input_petugas, input_buku
from proses_buku import hitung_total_halaman, rata_rata_halaman, buku_terbanyak


def main():
    print("=== APLIKASI DATA BUKU SEDERHANA ===\n")

    nama_petugas = input_petugas()
    daftar_buku, daftar_halaman = input_buku()

    total = hitung_total_halaman(daftar_halaman)
    rata = rata_rata_halaman(daftar_halaman)
    buku_max, halaman_max = buku_terbanyak(daftar_buku, daftar_halaman)

    print("\n=== HASIL DATA BUKU ===")
    print(f"Petugas: {nama_petugas}")

    print("\nDaftar Buku:")
    for i in range(3):
        print(f"{i+1}. {daftar_buku[i]} - {daftar_halaman[i]} halaman")

    print(f"\nTotal halaman: {total}")
    print(f"Rata-rata halaman: {rata:.2f}")
    print(f"Buku dengan halaman terbanyak: {buku_max} ({halaman_max} halaman)")


if _name_ == "_main_":
    main()