#menentukan input
b = input ("Masukkan bentuk yang diinginkan: ")
n = int (input("Masukkan tinggi bentuk: "))

#program segitiga siku2
if b == "Segitiga Siku-Siku":
    for i in range (1, n+1):
        print("*"*i)

#program persegi
if b == "Persegi":
    for j in range (1, n+1):
        print ("*"*n)

#program segitiga sama sisi
if b == "Segitiga Sama Sisi":
    for k in range (1, n+1):
        print (" "*(n-k), end="")
        print ("* "*k)
        

