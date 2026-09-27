nama = input("Masukkan Nama Anda: ")
NIM = input("Masukkan NIM Anda: ")

Menu_Misi = {
    "1": "Misi Standar dengan Bonus 2% dari Reward Dasar",
    "2": "Misi Sulit dengan Bonus 5% dari Reward Dasar",
    "3": "Misi Kritis dengan Bonus 8% dari Reward Dasar",
    "4": "Misi Penyelamatan Bumi dengan Bonus 12% dari Reward Dasar"
}

Misi_1 = "1. Misi Standar Dengan Bonus 2% Dari Reward Dasar"
Misi_2 = "2. Misi Sulit Dengan Bonus 5% Dari Reward Dasar"
Misi_3 = "3. Misi Kritis Dengan Bonus 8% Dari Reward Dasar"
Misi_4 = "4. Misi Penyelamatan Bumi Dengan Bonus 12% Dari Reward Dasar"

if nama == "Alya Nuryasmin" and NIM == "55":
    print("=====GREEN LANTERN CORPS MISSION=====")
    print(Misi_1)
    print(Misi_2)
    print(Misi_3)
    print(Misi_4)
    print("------------------------------------------------------------------------")
    
    Reward_Dasar = 1000
    misi = input("Pilih Misi: ")

    if misi == "1":
        Reward_Bonus = Reward_Dasar * 0.02
        print("Misi yang anda pilih adalah: ", Menu_Misi["1"])
    elif misi == "2":
        Reward_Bonus = Reward_Dasar * 0.05
        print("Misi yang anda pilih adalah: ", Menu_Misi["2"])
    elif misi == "3":
        Reward_Bonus = Reward_Dasar * 0.08
        print("Misi yang anda pilih adalah: ", Menu_Misi["3"])
    elif misi == "4":
        Reward_Bonus = Reward_Dasar * 0.12
        print("Misi yang anda pilih adalah: ", Menu_Misi["4"])
    else: 
        print("Misi tidak tersedia")
        Reward_Bonus = 0  
        
    if misi in ["1", "2", "3", "4"]:
        print("Reward bonus anda adalah: ", Reward_Bonus)
        Reward_Akhir = Reward_Dasar + Reward_Bonus
        print("Reward akhir anda adalah: ", Reward_Akhir)
        print("------------------------------------------------------------------------")

elif nama != "Alya Nuryasmin" and NIM != "55":
    print("Nama dan NIM yang anda masukkan salah")
elif nama != "Alya Nuryasmin":
    print("Nama yang anda masukkan salah")
elif NIM != "55":
    print("NIM yang anda masukkan salah")
