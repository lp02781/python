import math

#menentukan input
a = input ("")
b = input ("")
c = int (input (""))

#menentukan output
for i in range (1, c):
    print (a+b, end="")
print (a, end=" ")
    
#menentukan ganjil,genap,atau prima
prima=True
for x in range (2, c-1):
    if c%x==0:
        prima=False

if prima==True:
    print("(PRIMA)")
elif c%2==0:
    print("(GENAP)")
elif c%2==1:
    print("(GANJIL)")
