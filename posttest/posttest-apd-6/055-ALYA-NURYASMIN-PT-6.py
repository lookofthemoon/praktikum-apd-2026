print("==SELAMAT DATANG DI PROGRAM PENDATAAN WISHLIST==")

pengguna = {
    "Alya": "2609106055",
    "Al": "lookofthemoon"
}

koleksi = {
    "Album IVE": [
        "I've IVE I Ver.", "IVE EMPATHY ME Ver.", "IVE EMPATHY DIGIPACK ANYUJIN Ver.", 
        "IVE EMPATHY DIGIPACK GAEUL Ver.", "REVIVE+ Challengers Ver.", "REVIVE+ Bangers Ver.", 
        "Be Alright DIGIPACK REI Ver.", "IVE SWITCH LOVED IVE Ver.", "IVE SWITCH ON Ver.", 
        "IVE SWITCH OFF Ver.", "IVE SWITCH SPIN-OFF Ver.", "IVE SECRET LOVED IVE Ver.", 
        "IVE SECRET DIGIPACK GAEUL Ver.", "LOVE DIVE VERSION 1", "AFTER LIKE VERSION 3"
    ],
    "Album GFRIEND": [
        "Season Of Memories Standard Ver.", "VIVIZ MONTAGE OF() VIVID Ver.", "YUJU O A Ver."
    ],
    "Merchandise Game": [
        "Standee ZZZ Zhu Yuan", "Standee Genshin Impact Mavuika", "Standee Genshin Impact Raiden Shogun", 
        "Standee HI3 Raiden Mei", "Standee HI3 Kiana Kaslana", "Standee HSR Kafka", 
        "Standee ZZZ Astra Yao", "Keychain-keychain", "Plushie ZZZ Zhu Yuan", 
        "Plushie ZZZ Jane Doe", "Plushie Genshin Impact Mavuika", "Sticker-sticker"
    ]
}

wishlist = {
    "Album IVE": [
        "I'VE MINE LOVED IVE Ver.", "I'VE MINE OFF THE RECORD Ver.", 
        "I'VE MINE BADDIE Ver.", "I'VE MINE EITHER WAY Ver.", 
        "ELEVEN VERSION 1", "ELEVEN VERSION 2"
    ],
    "Album GFRIEND": [
        "TIME FOR US Daybreak Ver.", "TIME FOR US Daytime Ver.", 
        "TIME FOR US Midnight Ver.", "THE AWAKENING Knight Ver.", 
        "THE AWAKENING Military Ver.", "SNOWFLAKE"
    ],
    "Merchandise Game": [
        "Plushie Claire Ann Byers", "Plushie Luna Kim"
    ]
}

while True:
    print("=== SELAMAT DATANG DI PROGRAM PENDATAAN WISHLIST ===")
    print("")
    print("===================================================================")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar Program")
    print("===================================================================")
    pilihan_awal = input("Silahkan Pilih Opsi (1-3) : ")

    if pilihan_awal == "1":
        print("")
        print("=== SILAHKAN LOGIN ===")
        username = input("Masukkan Username Kamu : ")
        password = input("Masukkan Password Akun Kamu : ")

        if username in pengguna and pengguna[username] == password:
            
            if username == "Alya":
                while True:
                    print("===================================================================")
                    print("===== MENU AKSES ADMIN =====")
                    print("1. Tampilkan Koleksi Saat Ini")
                    print("2. Tampilkan Wishlist")
                    print("3. Keluar")
                    print("===================================================================")
                    
                    pilihan_admin = input("Silahkan Pilih Opsi (1-3) : ")
                    
                    if pilihan_admin == "1": 
                        print("===================================================================")
                        print("Berikut barang-barang yang berhasil kamu gapai untuk sekarang : ")
                        print("")
                        print("=============== ALBUM-ALBUM ===============")
                        print("ALBUM IVE : ")
                        for i in koleksi["Album IVE"]:
                            print("-", i)
                        print("")
                        print("ALBUM GFRIEND : ")
                        for j in koleksi["Album GFRIEND"]:
                            print("-", j)
                        print("")
                        print("=============== MERCHANDISES ===============")
                        for k in koleksi["Merchandise Game"]:
                            print("-", k)
                            
                        while True:
                            print("")
                            print("===================================================================")
                            print("MENU AKSES KHUSUS ADMIN")
                            print("1. Tambahkan Koleksi Baru Pada Kategori yang Ada")
                            print("2. Hapus Data Koleksi")
                            print("3. Ubah Barang Koleksi")
                            print("4. Keluar")
                            print("===================================================================")

                            pilihan2 = input("Silahkan Pilih Opsi (1-4) : ")
                            
                            if pilihan2 == "1":
                                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                                if kategori in koleksi:
                                    tambahkan_koleksi = input("Silahkan masukkan nama barang : ")
                                    koleksi[kategori].append(tambahkan_koleksi)
                                    print(f"Berhasil menambahkan '{tambahkan_koleksi}' ke Koleksi {kategori}!")
                                    print("")
                                    print("===================================================================")
                                    print("HASIL AKHIR KOLEKSI SETELAH PERUBAHAN:")
                                    print("=============== ALBUM-ALBUM ===============")
                                    print("ALBUM IVE : ")
                                    for i in koleksi["Album IVE"]:
                                        print("-", i)
                                    print("")
                                    print("ALBUM GFRIEND : ")
                                    for j in koleksi["Album GFRIEND"]:
                                        print("-", j)
                                    print("")
                                    print("=============== MERCHANDISES ===============")
                                    for k in koleksi["Merchandise Game"]:
                                        print("-", k)
                                else:
                                    print("Kategori yang kamu masukkan tidak terdeteksi.")
                                    
                            elif pilihan2 == "2":
                                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                                if kategori in koleksi:
                                    hapus_koleksi = input("Silahkan masukkan nama barang yang ingin dihapus : ")
                                    if hapus_koleksi in koleksi[kategori]:
                                        koleksi[kategori].remove(hapus_koleksi)
                                        print(f"Berhasil menghapus '{hapus_koleksi}' dari Koleksi {kategori}.")
                                        
                                        print("")
                                        print("===================================================================")
                                        print("HASIL AKHIR KOLEKSI SETELAH PERUBAHAN:")
                                        print("=============== ALBUM-ALBUM ===============")
                                        print("ALBUM IVE : ")
                                        for i in koleksi["Album IVE"]:
                                            print("-", i)
                                        print("")
                                        print("ALBUM GFRIEND : ")
                                        for j in koleksi["Album GFRIEND"]:
                                            print("-", j)
                                        print("")
                                        print("=============== MERCHANDISES ===============")
                                        for k in koleksi["Merchandise Game"]:
                                            print("-", k)
                                    else:
                                        print("Nama barang tidak ditemukan dalam koleksi.")
                                else:
                                    print("Kategori yang kamu masukkan tidak terdeteksi.")
                                    
                            elif pilihan2 == "3":
                                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                                if kategori in koleksi:
                                    lama = input("Masukkan nama barang lama yang ingin diganti: ")
                                    if lama in koleksi[kategori]:
                                        index_lama = koleksi[kategori].index(lama)
                                        baru = input("Masukkan nama barang baru: ")
                                        koleksi[kategori][index_lama] = baru
                                        print(f"Berhasil mengubah '{lama}' menjadi '{baru}'!")
                                        print("")
                                        print("===================================================================")
                                        print("HASIL AKHIR KOLEKSI SETELAH PERUBAHAN:")
                                        print("=============== ALBUM-ALBUM ===============")
                                        print("ALBUM IVE : ")
                                        for i in koleksi["Album IVE"]:
                                            print("-", i)
                                        print("")
                                        print("ALBUM GFRIEND : ")
                                        for j in koleksi["Album GFRIEND"]:
                                            print("-", j)
                                        print("")
                                        print("=============== MERCHANDISES ===============")
                                        for k in koleksi["Merchandise Game"]:
                                            print("-", k)
                                    else:
                                        print("Nama barang lama tidak ditemukan dalam koleksi.")
                                else:
                                    print("Kategori yang kamu masukkan tidak terdeteksi.")
                            elif pilihan2 == "4":
                                print("Keluar dari menu khusus admin...")
                                break
                            else:
                                print("Pilihan tidak valid.")

                    elif pilihan_admin == "2":
                        print("===================================================================")
                        print("Berikut barang-barang yang telah kamu masukkan ke Wishlist : ")
                        print("")
                        print("=============== ALBUM-ALBUM ===============")
                        print("ALBUM IVE : ")
                        for a in wishlist["Album IVE"]:
                            print("-", a)
                        print("")
                        print("ALBUM GFRIEND : ")
                        for b in wishlist["Album GFRIEND"]:
                            print("-", b)
                        print("")
                        print("=============== MERCHANDISES ===============")
                        for c in wishlist["Merchandise Game"]:
                            print("-", c)
                            
                        while True:
                            print("")
                            print("===================================================================")
                            print("MENU AKSES KHUSUS ADMIN")
                            print("1. Tambahkan Barang Baru Pada Kategori Wishlist yang Ada")
                            print("2. Hapus Barang Wishlist")
                            print("3. Ubah Barang Wishlist")
                            print("4. Keluar")
                            print("===================================================================")

                            pilihan2 = input("Silahkan Pilih Opsi (1-4) : ")
                            
                            if pilihan2 == "1":
                                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                                if kategori in wishlist:
                                    tambahkan_wishlist = input("Silahkan masukkan nama barang : ")
                                    wishlist[kategori].append(tambahkan_wishlist)
                                    print(f"Berhasil menambahkan '{tambahkan_wishlist}' ke Wishlist {kategori}!")
                                    
                                    print("")
                                    print("HASIL AKHIR WISHLIST SETELAH PERUBAHAN:")
                                    print("=============== ALBUM-ALBUM ===============")
                                    print("ALBUM IVE : ")
                                    for a in wishlist["Album IVE"]:
                                        print("-", a)
                                    print("")
                                    print("ALBUM GFRIEND : ")
                                    for b in wishlist["Album GFRIEND"]:
                                        print("-", b)
                                    print("")
                                    print("=============== MERCHANDISES ===============")
                                    for c in wishlist["Merchandise Game"]:
                                        print("-", c)
                                else:
                                    print("Kategori yang kamu masukkan tidak terdeteksi.")

                            elif pilihan2 == "2":
                                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                                if kategori in wishlist:
                                    hapus_wishlist = input("Silahkan masukkan nama barang yang ingin dihapus : ")
                                    if hapus_wishlist in wishlist[kategori]:
                                        wishlist[kategori].remove(hapus_wishlist)
                                        print(f"Berhasil menghapus '{hapus_wishlist}' dari Wishlist {kategori}.")
                                        
                                        print("")
                                        print("HASIL AKHIR WISHLIST SETELAH PERUBAHAN:")
                                        print("=============== ALBUM-ALBUM ===============")
                                        print("ALBUM IVE : ")
                                        for a in wishlist["Album IVE"]:
                                            print("-", a)
                                        print("")
                                        print("ALBUM GFRIEND : ")
                                        for b in wishlist["Album GFRIEND"]:
                                            print("-", b)
                                        print("")
                                        print("=============== MERCHANDISES ===============")
                                        for c in wishlist["Merchandise Game"]:
                                            print("-", c)
                                    else:
                                        print("Nama barang tidak ditemukan dalam wishlist.")
                                else:
                                    print("Kategori yang kamu masukkan tidak terdeteksi.")

                            elif pilihan2 == "3":
                                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                                if kategori in wishlist:
                                    lama = input("Masukkan nama barang lama yang ingin diganti: ")
                                    if lama in wishlist[kategori]:
                                        index_lama = wishlist[kategori].index(lama)
                                        baru = input("Masukkan nama barang baru: ")
                                        wishlist[kategori][index_lama] = baru
                                        print(f"Berhasil mengubah '{lama}' menjadi '{baru}'!")
                                        
                                        print("")
                                        print("HASIL AKHIR WISHLIST SETELAH PERUBAHAN:")
                                        print("=============== ALBUM-ALBUM ===============")
                                        print("ALBUM IVE : ")
                                        for a in wishlist["Album IVE"]:
                                            print("-", a)
                                        print("")
                                        print("ALBUM GFRIEND : ")
                                        for b in wishlist["Album GFRIEND"]:
                                            print("-", b)
                                        print("")
                                        print("=============== MERCHANDISES ===============")
                                        for c in wishlist["Merchandise Game"]:
                                            print("-", c)
                                    else:
                                        print("Nama barang lama tidak ditemukan dalam wishlist.")
                                else:
                                    print("Kategori yang kamu masukkan tidak terdeteksi.")
                                
                            elif pilihan2 == "4":
                                print("Keluar dari menu khusus admin...")
                                break
                            else:
                                print("Pilihan tidak valid.")

                    elif pilihan_admin == "3":
                        print("Kamu telah berhasil keluar dari program!")
                        break
                    else:
                        print("Pilihan menu admin tidak valid.")
            
            else:
                while True:
                    print("===================================================================")
                    print("===== MENU AKSES USER =====")
                    print("1. Tampilkan Koleksi Saat Ini")
                    print("2. Tampilkan Wishlist")
                    print("3. Keluar")
                    print("===================================================================")

                    pilihan_user = input("Silahkan Pilih Opsi (1-3) : ")
                    
                    if pilihan_user == "1": 
                        print("===================================================================")
                        print("Berikut barang-barang yang berhasil kamu gapai untuk sekarang : ")
                        print("")
                        print("=============== ALBUM-ALBUM ===============")
                        print("ALBUM IVE : ")
                        for i in koleksi["Album IVE"]:
                            print("-", i)
                        print("")
                        print("ALBUM GFRIEND : ")
                        for j in koleksi["Album GFRIEND"]:
                            print("-", j)
                        print("")
                        print("=============== MERCHANDISES ===============")
                        for k in koleksi["Merchandise Game"]:
                            print("-", k)

                    elif pilihan_user == "2":
                        print("===================================================================")
                        print("Berikut barang-barang yang telah kamu masukkan ke Wishlist : ")
                        print("")
                        print("=============== ALBUM-ALBUM ===============")
                        print("ALBUM IVE : ")
                        for a in wishlist["Album IVE"]:
                            print("-", a)
                        print("")
                        print("ALBUM GFRIEND : ")
                        for b in wishlist["Album GFRIEND"]:
                            print("-", b)
                        print("")
                        print("=============== MERCHANDISES ===============")
                        for c in wishlist["Merchandise Game"]:
                            print("-", c)

                    elif pilihan_user == "3":
                        print("Kamu telah berhasil keluar dari program!")
                        break
                    else:
                        print("Pilihan menu user tidak valid.")
        else:
            print("Username atau Password salah! Silahkan coba lagi.")

    elif pilihan_awal == "2":
        print("")
        print("=== REGISTER AKUN BARU ===")
        username_baru = input("Buat Username Baru : ")
        if username_baru in pengguna:
            print("Username sudah terdaftar! Silahkan gunakan username lain.")
        else:
            password_baru = input("Buat Password Baru : ")
            pengguna[username_baru] = password_baru
            print(f"Akun dengan username '{username_baru}' berhasil didaftarkan! Silahkan login.")

    elif pilihan_awal == "3":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, silahkan pilih 1, 2, atau 3.")