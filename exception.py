def main():
    line=input()
    word = line.split()
    hasil=1
    for element in word:
        try:
            val = int(element)
            hasil *=val
        except ValueError:
            pass
    print (hasil)
main()

a=range(1,4)
x=0
b=1
while True:
    try:
        print(a[x],end="")
    except IndexError:
        if x>0:
            break
        else:
            b+=1
    x+=b
