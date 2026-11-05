from data import pengguna
import pwinput

def login():
    print("\n=== SILAHKAN LOGIN ===")
    username = input("Masukkan Username Kamu : ")
    password = pwinput.pwinput(
        prompt="Masukkan Password Akun Kamu : ", mask="*"
    )

    try:
        if username in pengguna and pengguna[username] == password:
            return username
        else:
            print("Username atau Password salah! Silahkan coba lagi.")
            return None
    except Exception as e:
        print(f"Terjadi kesalahan sistem saat login: {e}")
        return None

def register():
    print("\n=== REGISTER AKUN BARU ===")
    username_baru = input("Buat Username Baru : ")
    if username_baru in pengguna:
        print("Username sudah terdaftar! Silahkan gunakan username lain.")
    else:
        password_baru = pwinput.pwinput(prompt="Buat Password Baru : ", mask="*")
        pengguna[username_baru] = password_baru
        print(
            f"Akun dengan username '{username_baru}' berhasil didaftarkan!"
            " Silahkan login."
        )