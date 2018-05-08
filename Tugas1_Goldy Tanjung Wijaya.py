import turtle               #mengimpor library turtle
from random import randint  #mengimpor library random

masukan_petal = turtle.Screen()     #mengatur kemunculan layar
petal= turtle.Turtle() #men-set petal sebagai variabel fungsi turtle
row1 = int(masukan_petal.numinput(petal, "Enter the number of rows ")) #menginput jumlah baris
print(row1) #mencetak jumlah baris
pxl = int(masukan_petal.numinput(petal, "Enter the square size (pixels): ")) #menginput ukuran kotak dalam pixel
print(pxl) #mencetak ukuran kotak
n = int(masukan_petal.numinput(petal, "Enter the number of petals of the flower: ")) #menginput jumlah petal bunga
print(n)

petal.penup()           #mengangkat kursor agar ketika berpindah tidak terjadi garis
petal.goto(0,200)       #memindahkan kursor ke koordinat x=0 y=200
petal.pendown()         #meletakkan kembali kursor

#perulangan dan mencetak petal
for x in range (1,n+1):
    turtle.colormode(255)       #mengatur warna yang tersedia (RGB)
    petal.color(randint(0,255),randint(0,255),randint(0,255))  #me random warna yang tercetak
    #mencetak sebuah petal
    petal.circle(100,90)
    petal.left(90)
    petal.circle(100,90)
    petal.setheading(360*x/n)  #mengatur sudut untuk mencetak petal selanjutnya

petal.penup()               #mengangkat kursor
petal.goto(-(row1*pxl)/2,0)       #berpindah ke posisi bawah
petal.pendown()             #

#perulangan mencetak persegi papan catur
#membuat persegi secara berulang
for y in range (1, row1+1):
    #membuat hanya satu baris
    for z in range (1, row1+1):
        turtle.colormode(255)
        petal.begin_fill()
        petal.color(randint(0,255), randint(0,255), randint(0,255))
        petal.forward(pxl)
        petal.left(90)
        petal.forward(pxl)
        petal.left(90)
        petal.forward(pxl)
        petal.left(90)
        petal.forward(pxl)
        petal.left(90)
        petal.forward(pxl)
        petal.end_fill()
    #berpindah ke titik bawah
    petal.penup()
    petal.left(180)         
    petal.forward(row1*pxl)
    petal.setheading(270)
    petal.forward(pxl)
    petal.setheading(0)
    petal.pendown()
    
