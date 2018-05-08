def faktorial(x):
    if x==0:
        return 1
    else:
        faktorial(x-1)  
    print(x)
print(faktorial(5))
