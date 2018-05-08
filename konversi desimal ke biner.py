jawab=""
bil = int(input("Masukkan angka dalam desimal:"))
while bil>0:
    jawab = str(bil%2)+jawab
    bil=bil//2
    
print (jawab)
