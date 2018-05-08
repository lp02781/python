from tkinter import *
from FigureCanvas import FigureCanvas
class DisplayFigures:
    def __init__(self):
        window = Tk()
        window.title("Display Figure")
        figure1=FigureCanvas(window,"line",width=100, height=100)
        figure1.grid(row=1, column=1)
        figure1=FigureCanvas(window,"rectangle",False, 100, 100)
        figure1.grid(row=1, column=2)
        figure1=FigureCanvas(window,"oval",False, 100, 100)
        figure1.grid(row=1, column=3)
        figure1=FigureCanvas(window,"arc",False, 100, 100)
        figure1.grid(row=1, column=4)
        figure1=FigureCanvas(window,"rectangle",True, 100, 100)
        figure1.grid(row=1, column=5)
        figure1=FigureCanvas(window,"oval",True, 100, 100)
        figure1.grid(row=1, column=6)
        figure1=FigureCanvas(window,"arc",True, 145, 100)
        figure1.grid(row=1, column=7)
        window.mainloop()
        
DisplayFigures()
        
        
        
        
