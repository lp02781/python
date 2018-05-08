'''
	Solusi Lab 3A 
	Prepared By : Hafizh Rafizal Adnan
'''

##Inisiasi input tinggi piramid
tinggi_piramid=int(input('Masukan Tinggi Piramid :'))

##Inisiasi nilai awal angka yang akan dicetak
counter=1;

## Looping mencetak piramid angka
for x in range(0,tinggi_piramid):
	for z in range(tinggi_piramid,x,-1):
		print(str(counter),end=' ')
		counter+=1
	print()	