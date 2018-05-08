import math
class Daster:
    #inisialisasi attribute
    def __init__(self, name="", HP=0, AttackDamage=0, HealAmount=0,SpecialMoves="", DamageSpecial=0, CooldownSpecial=0, elemen=""):
        self.name=name
        self.HP=HP
        self.AttackDamage= AttackDamage
        self.HealAmount= HealAmount
        self.SpecialMoves= SpecialMoves
        self.DamageSpecial= DamageSpecial
        self.CooldownSpecial=CooldownSpecial
        self.elemen=elemen
        self.kuldon=CooldownSpecial
        #TODO lengkapi constructor

    #TODO lengkapi method-method di bawah ini

    #Daster menyerang anotherDaster
    def attack(self, anotherDaster):
        anotherDaster.HP = anotherDaster.HP-self.AttackDamage #pengurangan HP daster lain berdasarkan attack damage daster 1
        self.kuldon+=1 #variabel kuldon untuk menghitung ketika kuldon sudah terpakai
        print(self.name+" menyerang "+anotherDaster.name+"\nHP "+anotherDaster.name+" menjadi ",anotherDaster.HP)

    #daster mengheal diri sendiri    
    def heal(self):
        self.HP = self.HP + self.HealAmount
        self.kuldon+=1
        print(self.name+" menyembuhkan diri \nHP "+self.name+" menjadi ",self.HP)

      
    #Daster menyerang anotherDaster menggunakan Special Moves
    #Method ini harus mereturn sebuah nilai boolean
    #True jika berhasil, False jika gagal menggunakan Special Moves

    #ketika menggunakan special moves
    def useSpecialMoves(self, anotherDaster):
        #ketika kuldon lebih dari CooldownSpecial, special moves bisa digunakan
        if self.kuldon>=self.CooldownSpecial:
            #3 argumen if/elif dibawah untuk keadaann kuat
            if self.elemen=="Air" and anotherDaster.elemen=="Api":
                anotherDaster.HP=anotherDaster.HP-(2*self.DamageSpecial)
                print (self.name+" menggunakan "+self.SpecialMoves+", itu sangat efektif!")
                print ("HP "+anotherDaster.name+" menjadi ",anotherDaster.HP)
                self.kuldon=0
                return True
            elif self.elemen=="Api" and anotherDaster.elemen=="Tumbuhan":
                anotherDaster.HP=anotherDaster.HP-(2*self.DamageSpecial)
                print (self.name+" menggunakan "+self.SpecialMoves+", itu sangat efektif!")
                print ("HP "+anotherDaster.name+" menjadi ",anotherDaster.HP)
                self.kuldon=0
                return True
            elif self.elemen=="Tumbuhan" and anotherDaster.elemen=="Air":
                anotherDaster.HP=anotherDaster.HP-(2*self.DamageSpecial)
                print (self.name+" menggunakan "+self.SpecialMoves+", itu sangat efektif!")
                print ("HP "+anotherDaster.name+" menjadi ",anotherDaster.HP)
                self.kuldon=0
                return True
            #3 argumen if/elif dibawah untuk keadaan lemah
            elif self.elemen=="Api" and anotherDaster.elemen=="Air":
                anotherDaster.HP=anotherDaster.HP-(math.floor(self.DamageSpecial/2))
                print (self.name+" menggunakan "+self.SpecialMoves+", itu sangat tidak efektif!")
                print ("HP "+anotherDaster.name+" menjadi ",anotherDaster.HP)
                self.kuldon=0
                return True
            elif self.elemen=="Air" and anotherDaster.elemen=="Tumbuhan":
                anotherDaster.HP=anotherDaster.HP-(math.floor(self.DamageSpecial/2))
                print (self.name+" menggunakan "+self.SpecialMoves+", itu sangat tidak efektif!")
                print ("HP "+anotherDaster.name+" menjadi ",anotherDaster.HP)
                self.kuldon=0
                return True
            elif self.elemen=="Tumbuhan" and anotherDaster.elemen=="Api":
                anotherDaster.HP=anotherDaster.HP-(math.floor(self.DamageSpecial/2))
                print (self.name+" menggunakan "+self.SpecialMoves+", itu sangat tidak efektif!")
                print ("HP "+anotherDaster.name+" menjadi ",anotherDaster.HP)
                self.kuldon=0
                return True
            #argumen dibawah untuk keadaan sama kuat
            elif ((self.elemen==anotherDaster.elemen)):
                anotherDaster.HP=anotherDaster.HP-(self.DamageSpecial)
                print (self.name+" menggunakan "+self.SpecialMoves+", itu tidak sangat efektif!")
                print ("HP "+anotherDaster.name+" menjadi ", anotherDaster.HP)
                self.kuldon=0
                return True
        #apabila specialmoves tidak bisa digunakan
        else:
            print ("Gagal menggunakan Special Moves, "+self.SpecialMoves+" masih mempunyai cooldown selama ",(self.CooldownSpecial-self.kuldon)," turn")
            self.kuldon+=0 #ketika special moves tidak bisa digunakan, kuldon tidak bertambah
            return False       
