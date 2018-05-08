
tinggi = int(input("masukkan tingi piramid"))
counter=0
for i in range (0, tinggi+1):
    for j in range (1,i+1):
        print(" ",end=" ")
    for h in range (tinggi,i,-1):
        print(str(counter), end=" ")
        counter+=1
    print()

    
for n in range (0, tinggi+1):
    for m in range (0,n):
        print("  ",end=" ")
    for o in range (tinggi,n,-1):
        print(str(counter), end=" ")
        counter+=1
    print()


