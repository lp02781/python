def prima(x, y):
	keluaran=" "
	for index in range(x):
		if (index==0 or index==1):
			continue
		elif (index % 2 !=0 and index % 3 !=0 and index % 4 !=0 and index % 5 !=0 and index % 6 !=0 and index % 7 !=0 and index % 8 !=0 and index % 9 !=0): 
			keluaran += y[index]
		elif (index == 2 or index == 3 or index == 5 or index == 7):
			keluaran += y[index]
		else:
			continue
	return keluaran

def Menu(urutan):
	menu=["","Huruf Prima","Palindrom","Reverse"]
	print("Menu",menu[urutan])
	kalimat=input("Masukkan sebuah kalimat: ")
	if urutan==1 :
		indeks=len(kalimat)
		kalimat=prima(indeks, kalimat)
		kalimat="Hurufnya adalah"+""kalimat""
	elif urutan==2 :
		if kalimat==kalimat[::-1]:
			kalimat="Kalimat ini Palindrom"
		else:
			kalimat="Kalimat ini bukan Palindrom"
	else:
		kalimat=kalimat[::-1]
		kalimat="Dibalik menjadi "+kalimat
	return kalimat

while(True):
	print("[1] Huruf Prima")
	print("[2] Palindrom")	
	print("[3] Reverse")
	print("[4] Keluar dari Program")
	pilihan=int(input("Pilihan anda: "))
	if (pilihan<=3 and pilihan>=1) :
		print(Menu(pilihan))
	elif (pilihan==4):
		break
	else: continue
	
	

	
