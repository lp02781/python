##Your Code Goes Here

#input kode dan nama
kode = input("Masukkan kode ujian: ")

if kode=='siap_un_cbt':
    
    nama = input ("Masukkan nama: ")

    #membaca file
    bacafile = open("soal_ujian.txt","r")
    bukafile = bacafile.readlines()
    gas=0           #increment
    x=0             #pembanding
    benar=0
    kunci=""

    #untuk memunculkan soal berulang-ulang
    while gas<len(bukafile):           #perhitungan nilai
        pilihan = bukafile[gas]            
        pisah = pilihan.split(";")          #memisahkan pilihan dari string pada text sumber 

        #deklarasi kunci jawaban
        if int(pisah[5])== 1:
            kunci='a'
        elif int(pisah[5])== 2:
            kunci='b'
        elif int(pisah[5])==3:
            kunci='c'
        elif int(pisah[5])==4:
            kunci='d'

        #memisahkan jawaban dan tulisannya
        print("    ",str(gas+1),".",pisah[0],"\n\ta.",pisah[1],"\n\tb.",pisah[2],"\n\tc.",pisah[3],"\n\td.",pisah[4],"\n")
        jawab = input("Jawaban Anda: ")

        #mengenali jawaban
        if jawab==kunci and gas<len(bukafile):
            lanjut = input("Jawaban Benar. Apakah ingin lanjut ke soal berikutnya? (Y/N)")
            benar=benar+1
        elif jawab!=kunci and gas<len(bukafile):
            lanjut = input("Jawaban Salah. Apakah ingin lanjut ke soal berikutnya? (Y/N)")
        elif jawab==kunci and gas==len(bukafile):
            print("Jawaban Benar.")
            benar=benar+1
           
        elif jawab!=kunci and gas==len(bukafile):
            print("Jawaban Salah")
              
            break

        #apabila input Y maka lanjut, apabila N tidak lanjut. Apabila input lainnya akan salah
        if lanjut=='Y':
            gas+=1
        elif lanjut=='N':
            break
        else:
            print("input salah")

    nilai=(benar/(gas+1))*100
    print("Ujian berakhir. Jumlah soal benar",benar," dari ",gas+1,"soal total. Nilai anda: ",int(nilai))
    #write hasil ke hasil.txt
    hasilnya = open('hasil.txt','w')
    hasilnya.write(nama+";"+str(gas)+";"+str(nilai))
    hasilnya.close()

else:
    print("kode salah")
