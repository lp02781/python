def hore(x):
    if x==0:
        print("hore")
    else:
        print("hip ", end="")
        hore(x-1)
    

hore(5)
