def permutasi(lst):
    hasil=[]
    if (len(lst)==1):
        hasil.append(lst)
        return hasil
    else:
        for i in lst:
            subList = lst.copy()
            subList.remove(i)
            hasilStlh=permutasi(subList)
            for kemungkinan in hasilStlh:
                hasil.append([i]+kemungkinan)
        return hasil

print(permutasi(["a",2,3,4]))
print("\n")

print([i for i in range (0,202,2)])
print("\n")
x=0
print([x for i in range (0,202,2)])
print("\n")
print([i+y for i in range (0,202,2) for y in range (5)])
