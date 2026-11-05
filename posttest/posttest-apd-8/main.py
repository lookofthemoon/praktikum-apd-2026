from auth import login, register
from data import koleksi, wishlist
from menu_admin import menu_admin
from menu_user import menu_user
from utils import header, menu_utama, validasi_pilihan_menu

def main():
    while True:
        header()
        menu_utama()
        pilihan_awal = input("Silahkan Pilih Opsi (1-3) : ")

        if not validasi_pilihan_menu(pilihan_awal, 3):
            print("Pilihan tidak valid! Masukkan angka antara 1 sampai 3.")
            continue

        if pilihan_awal == "1":
            username = login()
            if username:
                if username == "Alya":
                    menu_admin(koleksi, wishlist)
                else:
                    menu_user(koleksi, wishlist)

        elif pilihan_awal == "2":
            register()

        elif pilihan_awal == "3":
            print("Terima kasih telah menggunakan program ini!")
            break


if __name__ == "__main__":
    main()