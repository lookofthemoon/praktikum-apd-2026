from prettytable import ALL, PrettyTable
from utils import cetak_tabel_data, pilih_kategori, validasi_pilihan_menu

def kelola_data(target_data, nama_data):
    while True:
        tabel_kelola = PrettyTable()
        tabel_kelola.field_names = ["No", f"Menu Kelola {nama_data}"]
        tabel_kelola.align[f"Menu Kelola {nama_data}"] = "l"
        tabel_kelola.hrules = ALL

        tabel_kelola.add_row(
            [1, f"Tambahkan Barang Baru Pada Kategori {nama_data} yang Ada"]
        )
        tabel_kelola.add_row([2, f"Hapus Barang {nama_data}"])
        tabel_kelola.add_row([3, f"Ubah Barang {nama_data}"])
        tabel_kelola.add_row([4, "Kembali ke Menu Admin"])

        print("\n")
        print(tabel_kelola)

        pilihan2 = input("Silahkan Pilih Opsi (1-4) : ")
        if not validasi_pilihan_menu(pilihan2, 4):
            print("Pilihan tidak valid.")
            continue

        if pilihan2 == "1":
            kategori = pilih_kategori()
            if kategori in target_data:
                barang_baru = input("Silahkan masukkan nama barang : ")
                target_data[kategori].append(barang_baru)
                print(f"Berhasil menambahkan '{barang_baru}' ke {nama_data} {kategori}!")
                cetak_tabel_data(
                    target_data, f"HASIL AKHIR {nama_data.upper()} SETELAH PERUBAHAN:"
                )
            else:
                print("Kategori yang kamu masukkan tidak terdeteksi.")

        elif pilihan2 == "2":
            kategori = pilih_kategori()
            if kategori in target_data:
                hapus_barang = input("Silahkan masukkan nama barang yang ingin dihapus : ")
                try:
                    target_data[kategori].remove(hapus_barang)
                    print(
                        f"Berhasil menghapus '{hapus_barang}' dari {nama_data} {kategori}."
                    )
                    cetak_tabel_data(
                        target_data, f"HASIL AKHIR {nama_data.upper()} SETELAH PERUBAHAN:"
                    )
                except ValueError:
                    print(f"Nama barang tidak ditemukan dalam {nama_data}.")
            else:
                print("Kategori yang kamu masukkan tidak terdeteksi.")

        elif pilihan2 == "3":
            kategori = pilih_kategori()
            if kategori in target_data:
                lama = input("Masukkan nama barang lama yang ingin diganti: ")
                try:
                    index_lama = target_data[kategori].index(lama)
                    baru = input("Masukkan nama barang baru: ")
                    target_data[kategori][index_lama] = baru
                    print(f"Berhasil mengubah '{lama}' menjadi '{baru}'!")
                    cetak_tabel_data(
                        target_data, f"HASIL AKHIR {nama_data.upper()} SETELAH PERUBAHAN:"
                    )
                except ValueError:
                    print(f"Nama barang lama tidak ditemukan dalam {nama_data}.")
            else:
                print("Kategori yang kamu masukkan tidak terdeteksi.")

        elif pilihan2 == "4":
            print(f"Keluar dari menu kelola {nama_data}...")
            break

def menu_admin(koleksi, wishlist):
    while True:
        tabel_admin = PrettyTable()
        tabel_admin.field_names = ["No", "Menu Akses Admin"]
        tabel_admin.align["Menu Akses Admin"] = "l"
        tabel_admin.hrules = ALL

        tabel_admin.add_row([1, "Tampilkan & Kelola Koleksi Saat Ini"])
        tabel_admin.add_row([2, "Tampilkan & Kelola Wishlist"])
        tabel_admin.add_row([3, "Keluar"])

        print("\n")
        print(tabel_admin)

        pilihan_admin = input("Silahkan Pilih Opsi (1-3) : ")
        if not validasi_pilihan_menu(pilihan_admin, 3):
            print("Pilihan menu admin tidak valid!")
            continue

        if pilihan_admin == "1":
            cetak_tabel_data(
                koleksi,
                "Berikut barang-barang yang berhasil kamu gapai untuk sekarang : ",
            )
            kelola_data(koleksi, "Koleksi")

        elif pilihan_admin == "2":
            cetak_tabel_data(
            wishlist, "Berikut barang-barang yang telah kamu masukkan ke Wishlist :"
            )
            kelola_data(wishlist, "Wishlist")

        elif pilihan_admin == "3":
            print("Kamu telah berhasil keluar dari program!")
            break