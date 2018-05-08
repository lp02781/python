import math #mengimpor library math

#fungsi menghitung lingkaran
def luas_lingkaran(diameter):
    #TODO implementasikan fungsi yang menghitung luas dari sebuah lingkaran
    #Gunakan math.pi untuk mendapatkan nilai phi (diperlukan untuk menghitung luas lingkaran)
    luascircle = (math.pi*diameter*diameter)/4  #luas lingkaran
    return luascircle

#fungsi menghitung persegi
def luas_persegi(sisi):
    #TODO implementasikan fungsi yang menghitung luas dari sebuah persegi
    luassquare = sisi**2        #luas persegi
    return luassquare

#fungsi menentukan bilangan prima atau tidak
def isPrima(angka):
    #TODO implementasikan fungsi yang mengecek apakah angka merupakan bilangan prima
    if angka==1:
        prima=False
    if angka >1:
        prima = True
        for i in range (2, angka):
            if angka%i==0:
                prima = False
    return prima

#fungsi menentukan diskon dan harga yang terjadi setelah diskon
def harga_diskon(harga_asli, besar_diskon):
    #TODO implementasikan fungsi yang menghitung harga setelah diskon
    setelah_diskon = harga_asli-((besar_diskon/100)*harga_asli)
    return setelah_diskon
