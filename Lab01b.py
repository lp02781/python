import math
hari = int (input ("Masukkan Jumlah hari: "))
tahun = int( hari/365)
sisa_hari1 = int (hari%365)
bulan = int (sisa_hari1/30)
sisa_hari3= int (sisa_hari1%30)
minggu = int (sisa_hari3/7)
sisa_hari2= int (sisa_hari3%7)
print (hari, " hari adalah ", tahun, " tahun ", bulan, " bulan ", minggu, " minggu, dan ",sisa_hari2, "hari")
