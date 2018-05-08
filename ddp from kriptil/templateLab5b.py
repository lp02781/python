def ambilKata(kata, index):
    kata = kata.split()
    return kata[int(index) - 1]

try:
    inputKata = input("Masukkan sebuah kalimat : ")
    inputIndex = input("Masukkan index kata akan diambil :")
    print(ambilKata(inputKata, inputIndex))
except IndexError:
    print("IndexError : Tidak dapat mengambil kata")
    
