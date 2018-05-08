'''
def sumDigits(x):
    if x<10:
        return x
    else:
        return (x%10) + sumDigits(x//10)

print(sumDigits(126))
'''

def itungHI(kalimat):
    if len(kalimat)<2:
        return 0
    else:
        if kalimat[0]+kalimat[1]=="hi":
            return 1+itungHI(kalimat[1:])
        else:
            return itungHI(kalimat[1:])

print(itungHI("xxxhixxhi"))
