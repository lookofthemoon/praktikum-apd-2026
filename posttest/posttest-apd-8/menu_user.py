from prettytable import ALL, PrettyTable
from utils import cetak_tabel_data, validasi_pilihan_menu

def menu_user(koleksi, wishlist):
    while True:
        tabel_menu = PrettyTable()
        tabel_menu.field_names = ["No", "Menu Akses User"]
        tabel_menu.align["Menu Akses User"] = "l"
        tabel_menu.hrules = ALL

        tabel_menu.add_row([1, "Tampilkan Koleksi Saat Ini"])
        tabel_menu.add_row([2, "Tampilkan Wishlist"])
        tabel_menu.add_row([3, "Keluar"])

        print("\n")
        print(tabel_menu)

        pilihan_user = input("Silahkan Pilih Opsi (1-3) : ")
        if not validasi_pilihan_menu(pilihan_user, 3):
            print("Pilihan menu user tidak valid.")
            continue

        if pilihan_user == "1":
            cetak_tabel_data(
                koleksi,
                "Berikut barang-barang yang berhasil kamu gapai untuk sekarang : ",
            )
        elif pilihan_user == "2":
            cetak_tabel_data(
                wishlist, "Berikut barang-barang yang telah kamu masukkan ke Wishlist :"
            )
        elif pilihan_user == "3":
            print("Kamu telah berhasil keluar dari program!")
            break