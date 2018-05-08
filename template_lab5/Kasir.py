import Warung


#Tidak boleh mengubah isi file ini sedikitpun

#Jalankan file ini jika sudah selesai mengimplementasikan fungsi pada
#file Kalkulator.py dan Warung.py

print("Pembeli pertama datang!!!")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
pembeli1 = "Anto"
bill = 0
bill += Warung.beli_pizza(pembeli1, 7, "bulat")
bill += Warung.beli_mendoan(pembeli1, 4, "persegi")
bill += Warung.beli_martabak(pembeli1, 2, "bulat")
Warung.cetak(pembeli1, bill)
print("------------------------------------------------------------\n")

print("Pembeli kedua datang!!!")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
pembeli2 = "Budi"
bill = 0
bill += Warung.beli_pizza(pembeli2, 14, "persegi")
bill += Warung.beli_martabak(pembeli2, 15, "persegi")
bill += Warung.beli_mendoan(pembeli2, 6, "persegi")
Warung.cetak(pembeli2, bill)
print("------------------------------------------------------------\n")

print("Pembeli ketiga datang!!!")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
pembeli3 = "Steven"
bill = 0
bill += Warung.beli_mendoan(pembeli3, 23, "bulat")
Warung.cetak(pembeli3, bill)
print("------------------------------------------------------------\n")

print("Hari sudah malam, warung ditutup")
