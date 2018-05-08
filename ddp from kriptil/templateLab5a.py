def menu():
    print("Kalkulator Pak Chanek")
    print("[1] Tambah")
    print("[2] Kurang")
    print("[3] Kali")
    print("[4] Bagi")
    print("[5] Keluar dari program")


def tambah(angkaPertama, angkaKedua):
    return int(angkaPertama) + int(angkaKedua)


def kurang(angkaPertama, angkaKedua):
    return int(angkaPertama) - int(angkaKedua)


def kali(angkaPertama, angkaKedua):
    return int(angkaPertama) * int(angkaKedua)


def bagi(angkaPertama, angkaKedua):
    return int(angkaPertama) / int(angkaKedua)

try:
    apakahMasihMenghitung = True
    while (apakahMasihMenghitung):
        menu()
        pilihanPengguna = input("Pilihan saya :")
        if pilihanPengguna == 1 or pilihanPengguna == "1":
            inputPertama = input("Angka pertama : ")
            inputKedua = input("Angka kedua : ")
            print(inputPertama, "+", inputKedua, "=", tambah(inputPertama, inputKedua))
        elif pilihanPengguna == 2 or pilihanPengguna == "2":
            inputPertama = input("Angka pertama : ")
            inputKedua = input("Angka kedua : ")
            print(inputPertama, "-", inputKedua, "=", kurang(inputPertama, inputKedua))
        elif pilihanPengguna == 3 or pilihanPengguna == "3":
            inputPertama = input("Angka pertama : ")
            inputKedua = input("Angka kedua : ")
            print(inputPertama, "x", inputKedua, "=", (inputPertama, inputKedua))
        elif pilihanPengguna == 4 or pilihanPengguna == "4":
            inputPertama = input("Angka pertama : ")
            inputKedua = input("Angka kedua : ")
            print(inputPertama, "/", inputKedua, "=", bagi(inputPertama, inputKedua))
        elif pilihanPengguna == 5 or pilihanPengguna == "5":
            apakahMasihMenghitung = False
except ZeroDivisionError:
    print("ZeroDivisionError: Pembagi tidak boleh diisi nilai 0")
    
