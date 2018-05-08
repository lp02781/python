kata = input ("masukkan kata: ")
list (kata)
rotation = int(input ("masukkan banyaknya rotasi: "))
x=len(kata)
for y in range (0, x):
    a = ord(kata[y])+rotation
    b0 = chr(a)
    print(b0)

