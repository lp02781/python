def main():
    line=input()
    worldList=line.split()
    hasil=1
    for element in worldList:
        try:
            val=int(element)
            hasil *=val
        except ValueError:
                pass
    print (hasil)

main()
