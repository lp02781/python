"""
Contoh solusi Lab 6
author : Khoirul Khuluqi Abdulloh
Date   : 20 November 2017
Python 3
Perlu diperhatikan solusi ini hanyalah satu diantara banyak solusi
"""

#Menginisiasi sebuah dictionary yang akan meyimpan seluruh antrian
antrians = {}

#Looping untuk n perintah
for i in range(int(input())):
    perintah = input().split()

    #Perintah NEW
    if (perintah[0] == "NEW"):
        makanan = perintah[1]
        
        #Mengecek apakah antrian sudah ada
        if (makanan in antrians):
            print("Menu " + makanan + " sudah ada")
        else:
            #Membuat antrian baru yang masih kosong jika belum ada
            antrians[makanan]=[]
            print("Berhasil menambahkan antrian untuk menu " + makanan)

    #Perintah ADD
    elif (perintah[0] == "ADD"):
        makanan = perintah[1]

        #Mengecek apakah antrian ada
        if (makanan not in antrians):
            print("Tidak ada menu "+makanan)
        else:
            nama_pembeli = perintah[2]
            banyak_pesanan = perintah[3]

            #Menyatukan informasi nama dan banyak pesanan pembeli menggunakan sebuah list
            info_pembeli = [nama_pembeli, banyak_pesanan]

            #Memasukkan informasi tersebut ke dalam antrian
            antrians[makanan].append(info_pembeli)
            print(nama_pembeli + " mengantri untuk membeli " + makanan + " sebanyak " + banyak_pesanan + " porsi")
            
    #Perintah SERVE
    elif (perintah[0] == "SERVE"):
        makanan = perintah[1]

        #Mengecek apakah antrian ada
        if (makanan not in antrians):
            print("Tidak ada menu " + makanan)
        else:
            antrian=antrians[makanan]
            #Mengecek apakah antrian kosong
            if (len(antrian)>0):

                #Mengambil informasi pembeli terdepan sekaligus menghapusnya dari list
                info_pembeli = antrian.pop(0)
                nama = info_pembeli[0]
                banyak_pesanan = info_pembeli[1]
                print("Menyajikan {} porsi {} kepada {}, {} pulang dengan senang".format(banyak_pesanan, makanan, nama, nama))
            else:
                print("Antrian " + makanan + " kosong")

    #Perintah HABIS
    else:
        makanan = perintah[1]

        #Mengecek apakah antrian ada
        if (makanan not in antrians):
            print("Tidak ada menu " + makanan)
        else:

            #Menghapus antrian tersebut jika ada
            del antrians[makanan]
            print("Menu " + makanan + " telah habis dan antriannya ditutup")
