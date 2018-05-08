import math
pi = math.pi
import os
def cls() :
    os.system("cls")
def Kubus () :
    def Luas_kubus (sisi) :
        Luas_kubus = 6*sisi*sisi
        return Luas_kubus
    def volume_kubus (sisi) :
        Volume_kubus = sisi**3
        return Volume_kubus
    sisi=int(input("Masukkan panjangnya = "))
    print("Luas Kubus =",Luas_kubus(sisi))
    print("Volume Kubus =",volume_kubus(sisi))
def bola () :
    def Luas_bola (sisi) :
        Luas_bola = 4*pi*sisi*sisi
        return Luas_bola
    def volume_bola (sisi) :
        Volume_bola = 4/3 *pi* sisi**3
        return Volume_bola
    sisi =float(input("Masukkan jari-jarinya"))
    print("Luas bola =",round(Luas_bola(sisi)))
    print("Volume bola =",round(volume_bola(sisi)))
def kerucut () :
    def Luas_kerucut (jari,sisi) :
        Luas_alas = pi * jari**2
        Luas_selimut = pi*jari*sisi
        Luas_kerucut = Luas_alas + Luas_selimut
        return Luas_kerucut
    def volume_kerucut (jari,tinggi) :
        Volume_kerucut = 1/3 *pi *tinggi *jari**2
        return Volume_kerucut
    jari = float(input("Masukkan Jari-jarinya = "))
    sisi = float(input("Masukkan Sisi-sisinya = "))
    tinggi = float(input("Masukkan Tingginya = "))
    print("Luas Kerucut =",round(Luas_kerucut(jari,sisi)))
    print("Volume Kerucut =",round(volume_kerucut(jari,tinggi)))
def konfirmasi() :
    masukan = input("Program telah Selesai, ingin keluar(Y/N)")
    if masukan == 'Y':
        exit()
    elif masukan == 'N' :
        cls()
        utama()
    else :
        cls()
        print("Input Error")
        konfirmasi()
def utama() :
    print("Silahkan pilih objeknya")
    print("1. Kubus")
    print("2. Bola")
    print("3. Kerucut")
    print("4. Keluar")
    masukkan = input("Silahkan memilih = ")
    if masukkan== "1" :
        cls()
        Kubus()
    elif masukkan=="2" :
        cls()
        bola()
    elif masukkan=="3" :
        cls()
        kerucut()
    elif masukkan=="4" :
        exit()
    else :
        print("Input Error")
        cls()
        utama()
    konfirmasi()
print("Ini program penghitung luas dan volume benda 3 dimensi")        
utama()


