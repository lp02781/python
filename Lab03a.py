tinggi = int(input("Masukkan tinggi piramid: ")) #input tinggi segitiga
y=0                                    #deklarasi nilai y awal adalah 0
for x in range (0, tinggi):             #pengulangan pertama untuk tinggi segitiga
    for i in range (tinggi-x):          #pengulangan kedua untuk print per baris
        y=y+1                           #increment angka output
        print (y,"", end="")               #output
    print()                             #ganti baris


