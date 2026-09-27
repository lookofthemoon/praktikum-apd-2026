cuaca = "hujan"

if cuaca == "hujan":
    print("bawa payung/jas hujan")
    print("otw")
    print("telat dikit")
else: 
    print("tidak perlu bawa payung/jas hujan")
    print("tidak otw")
    print("sangat telat cuy")

budget = 60000
cuaca = "hujan"

if budget > 30000 and cuaca == "cerah":
    print("beli yoshinoya")
else:
    print("masak indomie ajah")

kendaraan = input("masukkan jenis kendaraan: ").lower().strip()

if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
elif kendaraan == "sepeda":
    tarif_parkir = 6700
else:
    tarif_parkir = 15000

print("Tarif parkir yang harus dibayar:", tarif_parkir)

bilangan = -5

status = "bilangan negatif" if bilangan < 0 else "bilangan positif"

print("bilangan adalah", status)

username = input("Masukkan username:").lower().strip()
password = input("Masukkan password:")

if username == "alya":
    if password == "alyak":
        print("Berhasil")
    else:
        print("Password salah")
else:
    print("Username salah")

angka = 10 / 6
print(f"angka {angka:.0f}")




