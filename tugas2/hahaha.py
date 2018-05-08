'''
def CaesarCipher(text):
    plain=['a','b','c','d','e','f','g','i','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range (0, len(text)):
        for x in range (0, len(plain)):
            if text[i]==plain[x]:
                text[i]==plain[x-3]
    return text

teks = "Foo Bar"
(CaesarCipher(teks))
print(teks)

import math

def nuker(angka):
    dpnkm = math.floor(angka)
    remainder = angka-dpnkm

    bitdpnkm = len(str(dpnkm))
    pembagi = 10**bitdpnkm
    bitrmndr = len(str(remainder)) - 2
    pembagi2 = 10**bitrmndr

    dpnkm/=pembagi
    remainder *= pembagi2
    print(dpnkm)
    print(remainder)
    return dpnkm+remainder
    

print(nuker(1.5))
'''
def readFileLine(filename, lineNumber):
    try:
        input_file = open(filename)
        lines = input_file.readlines()
        print (lines[lineNumber])
        input_file.close()
    except IndexError:
        print ('Your index is out of bound')
    except ValueError:
        print ('Please input the valid number')
    except IOError:
        print ('The file doesnt exist')
    except TypeError:
        print ('Type Error happen')
readFileLine ('text.txt', 3)
