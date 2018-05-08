def periksa_relasi(relasi):
    for i in relasi:
        if (i[0]>i[1]):
            return True
        else:
            return False

print(periksa_relasi([(1,0),(9,8),(4,7),(8,10)]))


