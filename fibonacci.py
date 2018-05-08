#program fibonacci
#0 1 1 2 3 5 8 13 21 ....

panjang=0
bil1 = 0
bil2 = 1
for n in range (0,panjang-2):
    if n<=1:
        
    if n==0 and n==1:
        continue
    else:
        bil3 = bil1 + bil2
        bil1 = bil2
        bil2 = bil3
    
print(bil3)
