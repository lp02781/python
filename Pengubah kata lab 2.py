
huruf = input ("Masukkan input kata: ")
print("1. Huruf Prima")
print("2. Palindrom")
print("3. Reverse")
print("4. Keluar dari Program")
b = input("Pilihan anda: ")

x = int(len(huruf))
i=0
if b == "1":
    while i<=x:
        for j in range (2, x-1):
            if i%j ==0:
                print(huruf[i])
        i+=1
            
                
            
elif b == '2':
    if huruf[::-1] == huruf:
        print("PALINDROM")
    else:
        print("BUKAN PALINDROM")
            
elif b =='3':
    for i in range (x-1, -1, -1):
        print(huruf[i], end=" ")
        
elif b == '4':
    while True:
        break
