from tkinter import *
objectA = Tk()
wide = Canvas(objectA, width=500, height=400)
wide.pack()
x0 = 275
x1 = 300
y0 = 10
y1 = 35
for index in range (10):
    wide.create_rectangle(x0,y0,x1,y1,fill="white")
    x0 = x0-25
    y0 = y0+25
    y1 = y1+25
objectA.mainloop()

    
