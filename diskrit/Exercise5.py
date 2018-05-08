dna = input ("masukkan konfigurasi DNA: ")
dnaLis = list (dna)
countA = dnaLis.count('A')
persen = ((len(dna)- countA)/len(dna))*100
print ("persentase C+G pada DNA adalah: ", persen)


