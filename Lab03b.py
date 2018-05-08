#deklarasi pilihan yang ada
print ("Pilihan Konversi:")
print ("1. Desimal ke Biner")
print ("2. Biner ke Desimal")
print ("3. Berhenti ")

#input opsi
opsi = int(input("Pilih Opsi: "))

f=[]                        #deklarasi list kosong untuk fungsi append

#proses opsi 1
if (opsi==1):
    bil= int(input("Berikan bilangan integer positif dalam representasi desimal:"))
    while (bil>0):
        c=bil%2
        bil=bil//2
        x=list(c)
        #proses membalik angka
        if (c!=0):
            f.append(1)        #memasukkan input angka ke list f
        else:
            f.append(0)
    print(*f[::-1], sep="")       #menghilangkan separator

#proses opsi 2
if (opsi==2):
    biner= input("Berikan bilangan integer positif dalam representasi biner:")
    y=len(biner)
    u=0                             #deklarasi nilai awal u
    for v in range (0,y):
        u = u + int (biner[v])*2**(y-1-v)       #u adalah rumus konversi
    print (u)

if (opsi==3):
    print("terimakasih telah menggunakan program kami")
    
