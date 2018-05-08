from tkinter import *
class ProcessButtonEvent:
    def __init__(self):
        self.counter=0
        window = Tk()
        label = Label (window, text="goldy ganteng")
        pencetanK= Button(window, text="oke", fg="red", bg="blue", command = self.processOK)
        pencetanN= Button(window, text="cancel", bg="red", fg="blue", command=self.processCancel)
        label.pack()
        pencetanK.pack()
        pencetanN.pack()
        window.mainloop()
        
    def __str__(self):
        return counter
    def processOK(self):
        self.counter+=1        
    def processCancel(self):
        self.counter-=1

ob = ProcessButtonEvent()
print(ob)
#print(kden) 
