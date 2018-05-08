import math
class Kalku():
    def __init__(self, bil1=0, bil2=0, bil3=0):
        self.bil1=bil1;
        self.bil2=bil2;
        self.bil3=bil3;
    def __str__(self):
        return "bil1 adalah {}, bil2 adalah {}, bil3 adalah {}".format(self.bil1, self.bil2,self.bil3)
    def tambah(self):
        return self.bil1+self.bil2+self.bil3
    def kurang (self):
        return self.bil1-self.bil2-self.bil3
    def kali (self):
        return self.bil1*self.bil2*self.bil3
    def pangkat(self):
        return self.bil1**self.bil2**self.bil3
    def akar(self):
        return math.sqrt(self.bil3)
    def getBil1(self,bil1):
        self.bil1=bil1
    def getBil2(self,bil2):
        self.bil2=bil2
    def getBil3(self,bil3):
        self.bil3=bil3

calc=Kalku()
calc.getBil1(3)
calc.getBil2(4)
calc.getBil3(1)
print("hasil kali: ",calc.kali())
print("hasil tambah: ",calc.tambah())
print("hasil kurang: ",calc.kurang())
print("hasil pangkat: ",calc.pangkat())
print("hasil akar: ",calc.akar())
print("hasil gabung:",(calc.kali()).__add__(calc.tambah()))
