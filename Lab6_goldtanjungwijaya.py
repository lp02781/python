perulangan= int(input(""))                                  #input seberapa banyak perintah akan diberikan (diterjemahkan menjadi perulangan)
dict_makanan = {}                                           #dictionary untuk menampung data makanan yang dimasukkan user
z=[]                                                        #list kosong untuk menampung list hasil append (nantinya digunakan list 2 dimensi)
#menjalankan program sejumlah perintah perulangan
for i in range (0,perulangan):
    perintah=input("")                                      #menginput perintah eksekusi
    y=perintah.split()                                      #memecah perintah per kata untuk diketahui inputnya berjenis apa (NEW,ADD,SERVE,HABIS), hasilnya adalah 
    z.append(y)                                             #memasukkan list y ke 
    makanan=z[i][1]
    
    if y[0]=='NEW':
        if y[1] not in dict_makanan:
            dict_makanan[makanan]=0
            print("Berhasil menambahkan antrian untuk menu "+y[1])
            print(dict_makanan)
        elif y[1] in dict_makanan:
            print("Menu "+y[1]+" sudah ada")
            print(dict_makanan)
    if y[0]=='ADD':
        for x in dict_makanan:
            if y[1] not in dict_makanan:
                print("Tidak ada menu "+y[1])
            else:
                print(y[2]+" mengantri untuk membeli "+y[1]+" sebanyak "+y[3]+" porsi")

    jml=y[3]
    name=y[2]
    if y[0]=='SERVE':
        if y[1] not in dict_makanan:
            print("Tidak ada menu "+y[1])
        elif y[1] in dict_makanan and dict_makanan.pop(y[1]):
            
            print("menyajikan "+jml+" porsi "+y[1]+" kepada "+name+", "+name+" pulang dengan senang")

        else: 
            print("Antrian "+y[1]+" kosong")
    if y[0]=='HABIS':
        if y[1] not in dict_makanan:
            print("Tidak ada menu "+y[1])
        else:
            print("menu "+y[1]+" telah habis dan antriannya ditutup")
            dict_makanan.pop(y[1])
            
