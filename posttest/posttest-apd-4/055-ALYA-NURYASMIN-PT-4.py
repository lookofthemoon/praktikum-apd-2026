username = "alya"
password = "2609106055"
percobaan = 3
login_berhasil = False

while percobaan > 0 and not login_berhasil:
    print(f"\nSisa Percobaan Login Anda: {percobaan}")
    input_user = input("Masukkan Username Anda : ").lower()
    input_password = input("Masukkan Password Anda : ")
    
    if input_user == username and input_password == password:
        print("\nLogin Anda Berhasil. Selamat Datang, alya!")
        login_berhasil = True
    else:
        if input_user != username and input_password == password:
            print("Mohon Maaf, Login Anda Gagal! Username yang Anda Masukkan Salah!")
        elif input_user == username and input_password != password:
                print("Mohon Maaf, Login Anda Gagal! Password yang Anda Masukkan Salah!")
        else:
            print("Mohon Maaf, Login Anda Gagal! Username dan Password yang Anda Masukkan Salah!")

        percobaan -= 1

if not login_berhasil:
    print("\nPercobaan Login Anda Telah Habis. Silahkan Coba Lagi Nanti :D")

else:
    total_porsi = 0
    penerima_manfaat = 0
    jumlah_reguler = 0
    jumlah_anak = 0
    jumlah_keluarga = 0

    while True:
        print("\n===================================")
        print("        MENU DISTRIBUSI PAKET         ")
        print("===================================")
        print("1. Paket Reguler  (1 porsi)")
        print("2. Paket Anak     (1 porsi)")
        print("3. Paket Keluarga (4 porsi)")
        print("4. Keluar Dari Program")

        paket_pilihan = input("Masukkan Jenis Paket yang Diinginkan (1-4): ")

        if paket_pilihan == "" or not paket_pilihan.isdigit():
            print("\nPilihan yang Anda Masukkan Tidak Valid. Silahkan Pilih Paket Kembali! (1-4)")
            continue

        pilihan = int(paket_pilihan)

        if pilihan == 4:
            print("\n==================================")
            print("\nTerima Kasih Telah Mengunjungi Kami")
            break
        elif pilihan < 1 or pilihan > 4:
            print("\nPilihan yang Anda Masukkan Tidak Valid. Silahkan Pilih Paket Kembali! (1-4)")
            continue

        while True:
            jumlah_paket = input("Masukkan Jumlah Paket yang Ingin Dipesan : ")

            if jumlah_paket == "" or not jumlah_paket.isdigit():
                print("\nJumlah paket tidak valid. Silakan masukkan angka.")
                continue

            jumlah_porsi = int(jumlah_paket)

            if jumlah_porsi <= 0:
                print("\nMinimal Paket yang Dipesan Adalah 1!")
                continue
            break

        if pilihan == 3:
            porsi_paket = 4
        else:
            porsi_paket = 1

        for i in range(jumlah_porsi):
            total_porsi += porsi_paket

        if pilihan == 1:
            jumlah_reguler += jumlah_porsi
            penerima_manfaat += jumlah_porsi * 1
            print(f"\nBerhasil Menambahkan {jumlah_porsi} Paket Reguler.")
        elif pilihan == 2:
            jumlah_anak += jumlah_porsi
            penerima_manfaat += jumlah_porsi * 1
            print(f"\nBerhasil Menambahkan {jumlah_porsi} Paket Anak.")
        elif pilihan == 3:
            jumlah_keluarga += jumlah_porsi
            penerima_manfaat += jumlah_porsi * 4
            print(f"\nBerhasil Menambahkan {jumlah_porsi} Paket Keluarga.")

    if total_porsi >= 20:
        bonus = "5 Paket Buah"
    elif total_porsi >= 10:
        bonus = "3 Botol Susu"
    elif total_porsi >= 5:
        bonus = "1 Paket Vitamin"
    else:
        bonus = "Tidak Ada Bonus"

    print("\n==================================")
    print(f"Paket Reguler: {jumlah_reguler} paket")
    print(f"Paket Anak: {jumlah_anak} paket")
    print(f"Paket Keluarga: {jumlah_keluarga} paket")
    print(f"Total Porsi: {total_porsi} porsi")
    print(f"Penerima Manfaat: {penerima_manfaat} orang")
    print(f"Bonus: {bonus}")
    print("====================================")
    print("Terimakasih Telah Melakukan Pemesanan. Pesanan akan dibagikan secara gratis sehingga tidak dibutuhkan pembayaran")