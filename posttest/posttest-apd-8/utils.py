from prettytable import ALL, PrettyTable

def header():
    judul = "SELAMAT DATANG DI PROGRAM PENDATAAN WISHLIST"
    garis = "=" * 67
    print(garis)
    print(f"===== {judul} =====")
    print(garis)

def menu_utama():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Menu Utama"]
    tabel.align["Menu Utama"] = "l"
    tabel.hrules = ALL
    tabel.add_row([1, "Login"])
    tabel.add_row([2, "Register Akun Baru"])
    tabel.add_row([3, "Keluar Program"])
    print("\n")
    print(tabel)

def validasi_pilihan_menu(pilihan, batas_maks):
    hasil_validasi = False
    try:
        angka = int(pilihan)
        if 1 <= angka <= batas_maks:
            hasil_validasi = True
    except ValueError:
        pass
    return hasil_validasi

def pilih_kategori():
    kategori_pilihan = input(
        "Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND /"
        " Merchandise Game) : "
    )
    return kategori_pilihan

def cetak_tabel_data(data_dict, judul_tabel):
    print("===================================================================")
    print(judul_tabel)
    print("")
    tabel = PrettyTable()
    tabel.field_names = ["No", "Kategori", "Nama Barang"]
    tabel.align["Nama Barang"] = "l"
    tabel.hrules = ALL
    no = 1
    for kategori, daftar_barang in data_dict.items():
        for barang in daftar_barang:
            tabel.add_row([no, kategori, barang])
            no += 1
    print(tabel)


