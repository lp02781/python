#menghitung jumlah karakter dan jumlah angka

#input kalimat dan angka
input_kalimat=input("Masukan kalimat: ") 
input_angka=int(input("Masukan angka: "))

#fungsi menghitung jumlah karakter
def HitungKalimat(input_kalimat):
    #menentukan best case
    if len(input_kalimat)==0:
        return 0
    else:
        #selagi i pada input_kalimat
        for i in input_kalimat:
            return 1 + HitungKalimat(input_kalimat[1:])     #rekursifnya
            #rekursif ditentukan dengan perhitungan pada kalimat secara "maju"

#fungsi menghitung angka
def HitungAngka(input_angka):
    #menentukan best case
    if input_angka<10:
        return input_angka
    else:
        return (input_angka%10) + HitungAngka(input_angka//10) #rekursifnya
        #rekursif ditentuksn dgn menjumlahkan angka yang sudah dibagi (floor) dan hasil modulo nya

#output
print("Banyak karakter: ",HitungKalimat(input_kalimat))
print("Hasil perhitungan:",HitungAngka(input_angka))

