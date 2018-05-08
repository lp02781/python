#Tugas DDP 1
#Athina Maria Angelica

#Imports
import os
import math

#Define Functions
'''
def title():
    cls()
    print("~Kalkulator Luas dan Volume Bangun Ruang~".center(os.get_terminal_size().columns))
'''
def menu():
    print("Silahkan pilih menu di bawah ini :")
    print("1. Kubus")
    print("2. Bola")
    print("3. Kerucut")
    print("4. Keluar")
    user_input = input("Angka menu pilihan : ")
    cls()
    if(user_input == "1"):
        rusuk = int(input("Panjang rusuk kubus : "))
        luas = 6*rusuk*rusuk
        volume = rusuk**3
        cls()
        print("Luas kubus = ",luas)
        print("Volume kubus = ",volume)
        return menu2()
    elif(user_input == "2"):
        rad = int(input("Jari-jari bola : "))
        luas = round(4*math.pi*(rad**2))
        volume = round(math.pi*(rad**3)*math.pi)
        cls()
        print("Luas bola = ",luas)
        print("Volume bola = ",volume)
        return menu2()
    elif(user_input == "3"):
        alas = int(input("Jari-jari alas : "))
        tinggi = int(input("Tinggi : "))
        side = int(input("Sisi miring : "))
        luas = round((math.pi*alas*alas)+(math.pi*alas*side))
        volume = round(math.pi*alas*alas*tinggi*1/3)
        cls()
        print("Luas kerucut = ",luas)
        print("Volume kerucut = ",volume)
        return menu2()
    elif(user_input == "4"):
        return exit()
    else:
        print("Mohon pilih angka 1-4 saja.")
        return menu()

def exit():
    os.system("exit")

def cls():
    os.system("cls")

def menu2():
    print("1. Kembali ke menu utama")
    print("2. Keluar")
    user_input = input("Angka menu pilihan : ")
    if(user_input == "1"):
        cls()
        #title()
        return menu()
    elif(user_input == "2"):
        cls()
        return exit()
    else:
        print("Mohon pilih angka 1 atau 2 saja")
        return menu2()

#Main Program
#title()
menu()
