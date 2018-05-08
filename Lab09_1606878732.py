class Poster:
    #revisi
    def __init__(self, name, HP, power):
        self.name = name
        self.HP = HP
        self.power = power
    def getNama(self):
        return self.name
    #digunakan pas fusion
    def __add__(self, other):
        self.HP=self.HP+other.HP
        self.power=self.power+other.power
        return self
    #digunakan pas boost
    def __mul__(self, mbus):
        self.power+=self.power*mbus
    #digunakan pas terkuat atau terlemah
    def __gt__(self, other):
        if self.power > other.power:
            return Poster, self.name, self.power
    def __lt__(self, other):
        if self.power < other.power:
            return Poster, self.name, self.power
    
    #tambahkan method method yang dibutuhkan Poster (clue : Overloading Operator)

class Buqi:
    def __init__(self, JumlahPoster):
        self.poster = []
        self.menang = 0
        for i in range(JumlahPoster):
            poster = input().split(" ")
            self.poster.append(Poster(poster[0],int(poster[1]),int(poster[2])))
    def terkuat(self):
        mx = Poster("nama",0,0)
        for i in range (len(self.poster)):
            if (mx < self.poster[i]):
                mx = self.poster[i]
        print(mx.name+" adalah Poster terkuat dengan power",mx.power)
        return mx
      
    def terlemah(self):
        mn = Poster("nama",1000000,1000000)
        for i in range (len(self.poster)):
            if (mn > self.poster[i]):
                mn = self.poster[i]
        print(mn.name+" adalah Poster terlemah dengan power",mn.power)
       
    def fusion(self,namaPoster1,namaPoster2, Nama):
        posterGabungan =  Poster(Nama,0,0)
        #revisi
        #index poster itu mencari apakah namaposter 1 dan 2 ada di poster
        IndexPoster1=self.cari_Poster(namaPoster1)
        IndexPoster2=self.cari_Poster(namaPoster2)
        if IndexPoster1 == -1:
            print(namaPoster1+" Tidak ada")
        elif IndexPoster2 == -1:
            print(namaPoster2+" Tidak ada") 
        else:
            posterGabungan.HP+= self.poster[self.cari_Poster(namaPoster1)].HP + self.poster[self.cari_Poster(namaPoster2)].HP
            posterGabungan.power += self.poster[self.cari_Poster(namaPoster1)].power + self.poster[self.cari_Poster(namaPoster2)].power
            self.poster.append(posterGabungan)
            print(namaPoster1+" melakukan FUSION dengan"+namaPoster2+" menjadi "+Nama)
    #lengkapi agar bisa mengeluarkan output sesuai yang diinginkan

    def fusion_all(self, Nama):
        posterGabungan =  Poster(Nama,0,0)
        for i in range (len(self.poster)):
            posterGabungan += self.poster[i]
        self.poster.append(posterGabungan)
        print("Gabungan semua Poster menjadi Mega Poster "+posterGabungan.name)
        #lengkapi agar bisa mengeluarkan output sesuai yang diinginkan
                               
    def battle(self, poster):
        battle=False
        for i in range (len(self.poster)):
            if (poster < self.poster[i]):
                battle=True
                break
        if battle:
            print("Buqi berhasil mengalahkan "+poster.name)
            self.menang+=1
        else:
            mx = Poster("nama",0,0)
            for i in range (len(self.poster)):
                if (mx < self.poster[i]):
                    mx= self.poster[i]
            print("Buqi kabur karena power Poster terkuat yang dia miliki hanya ",mx.power)
        #lengkapi agar bisa mengeluarkan output sesuai yang diinginkan
        #poster adalah sebuah objek 

    def boost(self, namaPoster):
        #revisi
        for i in range(len(self.poster)):
            if namaPoster != self.poster[i].name:
                print(namaPoster+" tidak ada")
                break
            else:
                if self.menang==0:
                    print("Tidak bisa BOOST karena belum pernah menang")
                    break
                else:
                    besar_boost=self.poster[self.cari_Poster(namaPoster)] * self.menang
        print("Power "+namaPoster+" meningkat ",self.menang," kali lipat")
                #lengkapi agar bisa mengeluarkan output sesuai yang diinginkan
                               
    def status(self, namaPoster):
        #revisi
        #tambahkan implementasi sendiri jika poster yang mau di print tidak ada
        for i in range(len(self.poster)):
            if namaPoster == self.poster[i].name:
                print(namaPoster+" tidak ada")
            else:
                print("Nama: "+namaPoster)
                print("HP: ",poster.HP)
                print("Power: ",poster.power)
                break
                #di break supaya ga ngulang2
            #print(self.poster[self.cari_Poster(namaPoster)])

    def cari_Poster(self, namaPoster):
        for i in range (len(self.poster)):
            if (self.poster[i].getNama == namaPoster):
                return i
        return -1

JumlahPoster = input("Masukan jumlah poster yang dimiliki : ")
Luqi = Buqi(int(JumlahPoster))
while(True):
    perintah = input().split(" ")
    if (perintah[0] == "TERKUAT"):
        Luqi.terkuat()
                               
    elif (perintah[0] == "TERLEMAH"):
        Luqi.terlemah()
                               
    elif (perintah[0] == "FUSION"):
        Luqi.fusion(perintah[1],perintah[2],perintah[3])
                               
    elif (perintah[0] == "FUSION_ALL"):
        Luqi.fusion_all(perintah[1])
                               
    elif (perintah[0] == "BATTLE"):
        poster = Poster(perintah[1],int(perintah[2]),int(perintah[3]))
        Luqi.battle(poster)
                               
    elif (perintah[0] == "BOOST"):
        Luqi.boost(perintah[1])
                               
    elif (perintah[0] == "STATUS"):
        #revisi
        Luqi.status(perintah[1])
                               
