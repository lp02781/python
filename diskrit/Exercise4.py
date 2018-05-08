import math
angka_awal = int (input ("masukkan angka awal: "))
print ("faktor-faktornya adalah:")
n = math.ceil (angka_awal**(1/2))
countX = 1
for a in range (1, n):
    hasil=angka_awal%a
    if hasil==0:
        x=angka_awal/a
        print (a, x)
        u = str (a)
        countX = len (u)+1
print ("jumlah faktor ada: ", countX, end='')
        
