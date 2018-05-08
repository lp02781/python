'''
	Solusi Lab 3B 
	Prepared By : Hafizh Rafizal Adnan
'''


## Fungsi untuk mengubah dari decimal ke biner
def DecimalToBin(desimal):
	result=''
	n = desimal
	while n>=1:
		mod=n%2
		n=n//2
		result=str(mod)+result
	print(result)

## Fungsi untuk mengubah dari biner ke desimal
def BinToDecimal(biner):
	result=0
	for x in range(0,len(str(biner))):
		pangkat = len(str(biner))-(x+1)
		result+=int(str(biner)[x])*(2**pangkat)
	print(result)

## Mencetak menu pilihan opsi
print("Pilihan Konversi :\n 1. Desimal ke Biner \n 2. Biner ke Desimal \n 3. Berhenti")
## Menyimpan opsi pilihan
opsi=int(input("Pilih Opsi :"))

## Melakukan looping program sampai user memilih menu nomor 3 (exit)
while opsi<3:
	if opsi==1:
		desimal = int(input("Berikan bilangan integer positif dalam representasi desimal: "))
		
		## Eksekusi fungsi desimal ke biner
		DecimalToBin(desimal)
	elif opsi==2:
		biner = int(input("Berikan bilangan integer positif dalam representasi biner: "))
		
		## Eksekusi fungsi biner ke desimal
		BinToDecimal(biner)

	## Meminta input user kembali 	
	opsi=int(input("Pilih Opsi :"))

## Terminate Program
exit()