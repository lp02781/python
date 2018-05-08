'''
def Vertical(a):
    if a<10:
        print(a)
    else:
        Vertical(a//10)
        print(a%10)

Vertical(3124)
'''

def fibo(x):
    bil1=0
    bil2=1
    ke_sekian=1
    while(ke_sekian<x):
        if bil1==0 and bil2==1:
            continue
            ke_sekian+=1
        else:
            nth=bil1+bil2
            bil1=bil2
            bil2=nth
            
    print(nth)
            
fibo(8)
