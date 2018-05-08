perulangan1= int(input(""))                                  #input seberapa banyak perintah pertama akan diberikan (diterjemahkan menjadi perulangan)
python=set()
java=set()
C=set()
#menjalankan program sejumlah perintah perulangan entri data bagian pertama
for i in range (0,perulangan1):
    perintah=input("")                                      #menginput perintah eksekusi
    memisahkan=perintah.split(";")                          #memecah perintah per kata yang dipisah tanda ;
    #percabangan menurut input nama bahasa pemrograman
    if memisahkan[1]=="python":
        python.add(memisahkan[0])
    elif memisahkan[1]=="java":
        java.add(memisahkan[0])
    elif memisahkan[1]=="c":
        C.add(memisahkan[0])
    else:
        print("tidak ada bahasa")                           #muncul tulisan apabila bahasa selain C, java atau python

perulangan2=int(input(""))                                  #input seberapa banyak perintah kedua akan diberikan (diterjemahkan menjadi perulangan)
#menjalankan program sejumlah perintah perulangan entri data bagian kedua
for j in range (perulangan2):
    perintah2=input("")                                     #menginput perintah eksekusi
    memisahkan2=perintah2.split()                           #memecah perintah per kata yang dipisah spasi
    #percabangan menurut input ADD, SHOW, atau SHOWALL
    if memisahkan2[0]=='ADD':
        #percabangan menurut input nama bahasa pemrograman
        if memisahkan2[2]=='C':
            C.add(memisahkan2[1])
            print("\nBerhasil menambahkan "+memisahkan2[1])
        elif memisahkan2[2]=='Python':
            python.add(memisahkan2[1])
            print("\nBerhasil menambahkan "+memisahkan2[1])
        elif memisahkan2[2]=='Java':
            java.add(memisahkan2[1])
            print("\nBerhasil menambahkan "+memisahkan2[1])
        else:
            print("tidak ada bahasa")                       #muncul tulisan apabila bahasa selain C, java atau python
    elif memisahkan2[0]=='SHOW':
        #percabangan menurut input nama bahasa pemrograman
        if memisahkan2[1]=='Python':
            print("\nPeserta yang hanya memiliki kemampuan pada "+memisahkan2[1]+" adalah")
            #menampilkan isi set python yang bukan anggota set java dan atau C
            for k in python-java-C:
                print("- "+k)
        elif memisahkan2[1]=='Java':
            print("\nPeserta yang hanya memiliki kemampuan pada "+memisahkan2[1]+" adalah")
            #menampilkan isi set Java yang bukan anggota set C dan atau python
            for k in java-python-C:
                print("- "+k)
        elif memisahkan2[1]=='C':
            print("\nPeserta yang hanya memiliki kemampuan pada "+memisahkan2[1]+" adalah")
            #menampilkan isi set C yang bukan anggota set java dan atau python
            for k in C-python-java:
                print("- "+k)
    elif memisahkan2[0]=='SHOWALL':
        #3 baris perintah pertama sama seperti perintah SHOW
        print("Peserta yang hanya memiliki kemampuan PYTHON adalah")
        for k in python-java-C:
            print("- "+k)
        print("\nPeserta yang hanya memiliki kemampuan JAVA adalah")
        for k in java-python-C:
            print("- "+k)
        print("\nPeserta yang hanya memiliki kemampuan C adalah")
        for k in C-python-java:
            print("- "+k)
        print("\nPeserta yang memiliki kemampuan PYTHON,JAVA,C adalah")
        #menampilkan anggota set python yang beririsan dengan anggota set java dan C
        for k in (python.intersection(java)).intersection(C):
            print("- "+k)
        print("\nPeserta yang memiliki kemampuan PYTHON dan JAVA adalah")
        #menampilkan anggota set python yang beririsan dengan anggota set java
        for k in python.intersection(java):
            print("- "+k)
        print("\nPeserta yang memiliki kemampuan PYTHON dan C adalah")
        #menampilkan anggota set python yang beririsan dengan set C
        for l in python.intersection(C):
            print("- "+l)
        print("\nPeserta yang memiliki kemampuan C dan Java  adalah")
        #menampilkan anggota set java yang beririsan dengan set C
        for m in java.intersection(C):
            print("- "+m)
