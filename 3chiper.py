kata = input ("masukan kata: ")
pisah = kata.split()
rotation=3
x=len(pisah)
def cipher(inputan):
    u=len(inputan)
    for y in range (0,u):
        a=ord(inputan[y])-rotation
        b1=chr(a)
        if a<=96:
            b=ord(inputan[y])+26-rotation
            b1=chr(b)
    return b1




