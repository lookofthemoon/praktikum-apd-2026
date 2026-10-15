print("==SELAMAT DATANG DI PROGRAM PENDATAAN WISHLIST==")
username = input("Login Dulu Yuk! Masukkan Username Kamu : ")
password = input("Masukkan Password Akun Kamu : ")

koleksi_ive = ["I've IVE I Ver.", "IVE EMPATHY ME Ver.", "IVE EMPATHY DIGIPACK ANYUJIN Ver.", "IVE EMPATHY DIGIPACK GAEUL Ver.", "REVIVE+ Challengers Ver.", "REVIVE+ Bangers Ver.", "Be Alright DIGIPACK REI Ver.", "IVE SWITCH LOVED IVE Ver.", "IVE SWITCH ON Ver.", "IVE SWITCH OFF Ver.", "IVE SWITCH SPIN-OFF Ver.", "IVE SECRET LOVED IVE Ver.", "IVE SECRET DIGIPACK GAEUL Ver.", "LOVE DIVE VERSION 1", "AFTER LIKE VERSION 3"]
koleksi_gfriend = ["Season Of Memories Standard Ver.", "VIVIZ MONTAGE OF() VIVID Ver.", "YUJU O A Ver."]
koleksi_merchandise_game = ["Standee ZZZ Zhu Yuan", "Standee Genshin Impact Mavuika", "Standee Genshin Impact Raiden Shogun", "Standee HI3 Raiden Mei", "Standee HI3 Kiana Kaslana", "Standee HSR Kafka", "Standee ZZZ Astra Yao", "Keychain-keychain", "Plushie ZZZ Zhu Yuan", "Plushie ZZZ Jane Doe", "Plushie Genshin Impact Mavuika", "Sticker-sticker"]

wishlist_ive = ["I'VE MINE LOVED IVE Ver.", "I'VE MINE OFF THE RECORD Ver.", "I'VE MINE BADDIE Ver.", "I'VE MINE EITHER WAY Ver.", "ELEVEN VERSION 1", "ELEVEN VERSION 2"]
wishlist_gfriend = ["TIME FOR US Daybreak Ver.", "TIME FOR US Daytime Ver.", "TIME FOR US Midnight Ver.", "THE AWAKENING Knight Ver.", "THE AWAKENING Military Ver.", "SNOWFLAKE"]
wishlist_merchandise_game = ["Plushie Claire Ann Byers", "Plushie Luna Kim"]

if username == "Alya" and password == "2609106055":
    print("===================================================================")
    print("Kamu Berhasil Login dan Mendapatkan Akses Khusus Sebagai Admin!")
    print("")
    print("=====MENU AKSES ADMIN=====")
    print("1. Tampilkan Koleksi Saat Ini")
    print("2. Tampilkan Wishlist")
    print("3. Keluar")
    print("===================================================================")
    
    pilihan_admin = input("Silahkan Pilih Opsi (1-3) : ")
    
    if pilihan_admin == "1": 
        print("===================================================================")
        print("Berikut barang-barang yang berhasil kamu gapai untuk sekarang : ")
        print("")
        print("===============ALBUM-ALBUM===============")
        print("ALBUM IVE : ")
        for i in koleksi_ive:
            print("-", i)
        print("")
        print("ALBUM GFRIEND : ")
        for j in koleksi_gfriend:
            print("-", j)
        print("")
        print("===============MERCHANDISES===============")
        for k in koleksi_merchandise_game:
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
                if kategori == "Album IVE":
                    tambahkan_koleksi = input("Silahkan masukkan nama Album : ")
                    koleksi_ive.append(tambahkan_koleksi)
                    print(f"Berhasil menambahkan '{tambahkan_koleksi}' ke Koleksi Album IVE!")
                elif kategori == "Album GFRIEND":
                    tambahkan_koleksi = input("Silahkan masukkan nama Album : ")
                    koleksi_gfriend.append(tambahkan_koleksi)
                    print(f"Berhasil menambahkan '{tambahkan_koleksi}' ke Koleksi Album GFRIEND!")
                elif kategori == "Merchandise Game":
                    tambahkan_koleksi = input("Silahkan masukkan nama Merchandise : ")
                    koleksi_merchandise_game.append(tambahkan_koleksi)
                    print(f"Berhasil menambahkan '{tambahkan_koleksi}' ke Koleksi Merchandise Game!")
                else:
                    print("Kategori yang kamu masukkan tidak terdeteksi.")

                print("")
                print("===================================================================")
                print("HASIL AKHIR KOLEKSI SETELAH PERUBAHAN:")
                print("===============ALBUM-ALBUM===============")
                print("ALBUM IVE : ")
                for i in koleksi_ive:
                    print("-", i)
                print("\nALBUM GFRIEND : ")
                for j in koleksi_gfriend:
                    print("-", j)
                print("\n===============MERCHANDISES===============")
                for k in koleksi_merchandise_game:
                    print("-", k)
                print("===================================================================")
                    
            elif pilihan2 == "2":
                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                if kategori == "Album IVE":
                    hapus_koleksi = input("Silahkan masukkan nama Album yang ingin dihapus : ")
                    if hapus_koleksi in koleksi_ive:
                        koleksi_ive.remove(hapus_koleksi)
                        print(f"Berhasil menghapus '{hapus_koleksi}' dari Koleksi Album IVE.")
                    else:
                        print("Nama album tidak ditemukan dalam koleksi.")
                elif kategori == "Album GFRIEND":
                    hapus_koleksi = input("Silahkan masukkan nama Album yang ingin dihapus : ")
                    if hapus_koleksi in koleksi_gfriend:
                        koleksi_gfriend.remove(hapus_koleksi)
                        print(f"Berhasil menghapus '{hapus_koleksi}' dari Koleksi Album GFRIEND.")
                    else:
                        print("Nama album tidak ditemukan dalam koleksi.")
                elif kategori == "Merchandise Game":
                    hapus_koleksi = input("Silahkan masukkan nama Merchandise yang ingin dihapus : ")
                    if hapus_koleksi in koleksi_merchandise_game:
                        koleksi_merchandise_game.remove(hapus_koleksi)
                        print(f"Berhasil menghapus '{hapus_koleksi}' dari Koleksi Merchandise Game.")
                    else:
                        print("Nama merchandise tidak ditemukan dalam koleksi.")
                else:
                    print("Kategori yang kamu masukkan tidak terdeteksi.")
            
                print("")
                print("===================================================================")
                print("HASIL AKHIR KOLEKSI SETELAH PERUBAHAN:")
                print("===============ALBUM-ALBUM===============")
                print("ALBUM IVE : ")
                for i in koleksi_ive:
                    print("-", i)
                print("")
                print("ALBUM GFRIEND : ")
                for j in koleksi_gfriend:
                    print("-", j)
                print("")
                print("===============MERCHANDISES===============")
                for k in koleksi_merchandise_game:
                    print("-", k)
            elif pilihan2 == "3":
                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                if kategori == "Album IVE":
                    lama = input("Masukkan nama Album lama yang ingin diganti: ")
                    if lama in koleksi_ive:
                        index_lama = koleksi_ive.index(lama)
                        baru = input("Masukkan nama Album baru: ")
                        koleksi_ive[index_lama] = baru
                        print(f"Berhasil mengubah '{lama}' menjadi '{baru}'!")
                    else:
                        print("Nama Album lama tidak ditemukan dalam koleksi.")
                elif kategori == "Album GFRIEND":
                    lama = input("Masukkan nama Album lama yang ingin diganti: ")
                    if lama in koleksi_gfriend:
                        index_lama = koleksi_gfriend.index(lama)
                        baru = input("Masukkan nama Album baru: ")
                        koleksi_gfriend[index_lama] = baru
                        print(f"Berhasil mengubah '{lama}' menjadi '{baru}'!")
                    else:
                        print("Nama album lama tidak ditemukan dalam koleksi.")
                elif kategori == "Merchandise Game":
                    lama = input("Masukkan nama Merchandise lama yang ingin diganti: ")
                    if lama in koleksi_merchandise_game:
                        index_lama = koleksi_merchandise_game.index(lama)
                        baru = input("Masukkan nama merchandise BARU: ")
                        koleksi_merchandise_game[index_lama] = baru
                        print(f"Berhasil mengubah '{lama}' menjadi '{baru}'!")
                    else:
                        print("Nama merchandise lama tidak ditemukan.")
                else:
                    print("Kategori yang kamu masukkan tidak terdeteksi.")

                print("")
                print("===================================================================")
                print("HASIL AKHIR KOLEKSI SETELAH PERUBAHAN:")
                print("===============ALBUM-ALBUM===============")
                print("ALBUM IVE : ")
                for i in koleksi_ive:
                    print("-", i)
                print("")
                print("ALBUM GFRIEND : ")
                for j in koleksi_gfriend:
                    print("-", j)
                print("")
                print("===============MERCHANDISES===============")
                for k in koleksi_merchandise_game:
                    print("-", k)

            elif pilihan2 == "4":
                print("Kamu telah berhasil keluar dari program!")
                break
            else:
                print("Pilihan tidak valid.")

    elif pilihan_admin == "2":
        print("===================================================================")
        print("Berikut barang-barang yang telah kamu masukkan ke Wishlist : ")
        print("")
        print("===============ALBUM-ALBUM===============")
        print("ALBUM IVE : ")
        for a in wishlist_ive:
            print("-", a)
        print("")
        print("ALBUM GFRIEND : ")
        for b in wishlist_gfriend:
            print("-", b)
        print("")
        print("===============MERCHANDISES===============")
        for c in wishlist_merchandise_game:
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
                if kategori == "Album IVE":
                    tambahkan_wishlist = input("Silahkan masukkan nama Album : ")
                    wishlist_ive.append(tambahkan_wishlist)
                    print(f"Berhasil menambahkan '{tambahkan_wishlist}' ke Wishlist Album IVE!")
                elif kategori == "Album GFRIEND":
                    tambahkan_wishlist = input("Silahkan masukkan nama Album : ")
                    wishlist_gfriend.append(tambahkan_wishlist)
                    print(f"Berhasil menambahkan '{tambahkan_wishlist}' ke Wishlist Album GFRIEND!")
                elif kategori == "Merchandise Game":
                    tambahkan_wishlist = input("Silahkan masukkan nama Merchandise : ")
                    wishlist_merchandise_game.append(tambahkan_wishlist)
                    print(f"Berhasil menambahkan '{tambahkan_wishlist}' ke Wishlist Merchandise Game!")
                else:
                    print("Kategori yang kamu masukkan tidak terdeteksi.")

                print("")
                print("HASIL AKHIR WISHLIST SETELAH PERUBAHAN:")
                print("===============ALBUM-ALBUM===============")
                print("ALBUM IVE : ")
                for a in wishlist_ive:
                    print("-", a)
                print("\nALBUM GFRIEND : ")
                for b in wishlist_gfriend:
                    print("-", b)
                print("\n===============MERCHANDISES===============")
                for c in wishlist_merchandise_game:
                    print("-", c)
                    
            elif pilihan2 == "2":
                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                if kategori == "Album IVE":
                    hapus_wishlist = input("Silahkan masukkan nama Album yang ingin dihapus : ")
                    if hapus_wishlist in wishlist_ive:
                        wishlist_ive.remove(hapus_wishlist)
                        print(f"Berhasil menghapus '{hapus_wishlist}' dari Wishlist Album IVE.")
                    else:
                        print("Nama album tidak ditemukan dalam wishlist.")
                elif kategori == "Album GFRIEND":
                    hapus_wishlist = input("Silahkan masukkan nama Album yang ingin dihapus : ")
                    if hapus_wishlist in wishlist_gfriend:
                        wishlist_gfriend.remove(hapus_wishlist)
                        print(f"Berhasil menghapus '{hapus_wishlist}' dari Wishlist Album GFRIEND.")
                    else:
                        print("Nama album tidak ditemukan dalam wishlist.")
                elif kategori == "Merchandise Game":
                    hapus_wishlist = input("Silahkan masukkan nama Merchandise yang ingin dihapus : ")
                    if hapus_wishlist in wishlist_merchandise_game:
                        wishlist_merchandise_game.remove(hapus_wishlist)
                        print(f"Berhasil menghapus '{hapus_wishlist}' dari Wishlist Merchandise Game.")
                    else:
                        print("Nama merchandise tidak ditemukan dalam wishlist.")
                else:
                    print("Kategori yang kamu masukkan tidak terdeteksi.")

                print("")
                print("HASIL AKHIR WISHLIST SETELAH PERUBAHAN:")
                print("===============ALBUM-ALBUM===============")
                print("ALBUM IVE : ")
                for a in wishlist_ive:
                    print("-", a)
                print("\nALBUM GFRIEND : ")
                for b in wishlist_gfriend:
                    print("-", b)
                print("\n===============MERCHANDISES===============")
                for c in wishlist_merchandise_game:
                    print("-", c)

            elif pilihan2 == "3":
                kategori = input("Apakah kategori dari barang tersebut? (Album IVE / Album GFRIEND / Merchandise Game) : ")
                if kategori == "Album IVE":
                    lama = input("Masukkan nama Album lama yang ingin diganti: ")
                    if lama in wishlist_ive:
                        index_lama = wishlist_ive.index(lama)
                        baru = input("Masukkan nama Album baru: ")
                        wishlist_ive[index_lama] = baru
                        print(f"Berhasil mengubah '{lama}' menjadi '{baru}'!")
                    else:
                        print("Nama Album lama tidak ditemukan dalam koleksi.")
                elif kategori == "Album GFRIEND":
                    lama = input("Masukkan nama Album lama yang ingin diganti: ")
                    if lama in wishlist_gfriend:
                        index_lama = wishlist_gfriend.index(lama)
                        baru = input("Masukkan nama Album baru: ")
                        wishlist_gfriend[index_lama] = baru
                        print(f"Berhasil mengubah '{lama}' menjadi '{baru}'!")
                    else:
                        print("Nama album lama tidak ditemukan dalam koleksi.")
                elif kategori == "Merchandise Game":
                    lama = input("Masukkan nama Merchandise lama yang ingin diganti: ")
                    if lama in wishlist_merchandise_game:
                        index_lama = wishlist_merchandise_game.index(lama)
                        baru = input("Masukkan nama merchandise BARU: ")
                        wishlist_merchandise_game[index_lama] = baru
                        print(f"Berhasil mengubah '{lama}' menjadi '{baru}'!")
                    else:
                        print("Nama merchandise lama tidak ditemukan.")
                else:
                    print("Kategori yang kamu masukkan tidak terdeteksi.")
                
                print("")
                print("HASIL AKHIR WISHLIST SETELAH PERUBAHAN:")
                print("===============ALBUM-ALBUM===============")
                print("ALBUM IVE : ")
                for a in wishlist_ive:
                    print("-", a)
                print("\nALBUM GFRIEND : ")
                for b in wishlist_gfriend:
                    print("-", b)
                print("\n===============MERCHANDISES===============")
                for c in wishlist_merchandise_game:
                    print("-", c)

            elif pilihan2 == "4":
                print("Kamu telah berhasil keluar dari program!")
                break
            else:
                print("Pilihan tidak valid.")

    elif pilihan_admin == "3":
        print("Kamu telah berhasil keluar dari program!")
    else:
        print("Pilihan menu admin tidak valid.")
        
elif username == "Al" and password == "lookofthemoon":
    print("===================================================================")
    print("Kamu Berhasil Login Sebagai User!")
    print("")
    print("=====MENU AKSES USER=====")
    print("1. Tampilkan Koleksi Saat Ini")
    print("2. Tampilkan Wishlist")
    print("3. Keluar")
    print("===================================================================")

    pilihan_user = input("Silahkan Pilih Opsi (1-3) : ")
    
    if pilihan_user == "1": 
        print("===================================================================")
        print("Berikut barang-barang yang berhasil kamu gapai untuk sekarang : ")
        print("")
        print("===============ALBUM-ALBUM===============")
        print("ALBUM IVE : ")
        for i in koleksi_ive:
            print("-", i)
        print("")
        print("ALBUM GFRIEND : ")
        for j in koleksi_gfriend:
            print("-", j)
        print("")
        print("===============MERCHANDISES===============")
        for k in koleksi_merchandise_game:
            print("-", k)

    elif pilihan_user == "2":
        print("===================================================================")
        print("Berikut barang-barang yang telah kamu masukkan ke Wishlist : ")
        print("")
        print("===============ALBUM-ALBUM===============")
        print("ALBUM IVE : ")
        for a in wishlist_ive:
            print("-", a)
        print("")
        print("ALBUM GFRIEND : ")
        for b in wishlist_gfriend:
            print("-", b)
        print("")
        print("===============MERCHANDISES===============")
        for c in wishlist_merchandise_game:
            print("-", c)

    elif pilihan_user == "3":
        print("Kamu telah berhasil keluar dari program!")
    else:
        print("Pilihan menu user tidak valid.")

elif username == "Al" and password != "lookofthemoon":
    print("Sepertinya password yang kamu masukkan salah deh, Silahkan ulang program dan login kembali :D")
elif username != "Al" and password == "lookofthemoon":
    print("Sepertinya username yang kamu masukkan salah deh, Silahkan ulang program dan login kembali :D")
elif username == "Alya" and password != "2609106055":
    print("Sepertinya password yang kamu masukkan salah deh, Silahkan ulang program dan login kembali :D")
elif username != "Alya" and password == "2609106055":
    print("Sepertinya username yang kamu masukkan salah deh, Silahkan ulang program dan login kembali :D")
else:
    print("Sepertinya username dan password yang kamu masukkan salah deh, Silahkan ulang program dan login kembali :D")
