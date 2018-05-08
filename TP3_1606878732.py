#OOP tentara buat menyimpan data tentara berupa nama, umur, kuat, level
class Tentara():
    def __init__(self, jenis, nama="", umur=0,kuat=0,level=1):
        self.__jenis=jenis
        self.__nama=nama
        self.__umur=int(umur)
        self.__kuat=int(kuat)
        self.__level=int(1)
    def __str__(self):
        return "{} berusia {} tahun, kekuatan: {}, level: {}".format(self.__nama, self.__umur, self.__kuat, self.__level)
    def getNama (self):
        return self.__nama
    def getJenis (self):
        return self.__jenis
    def getKuat (self):
        return self.__kuat
    def tambahKuat (self, kuat):
        self.__kuat+=kuat
    def tambahLevel(self, levelOps):
        self.__level+=levelOps

JenisSoldier=set()  #menampung nama jenis tentara seperti sniper dll
namasoldier=[]      #menampung nama-nama tentara yang merupakan object
JenisOperasi={}     #menampung jenis-jenis operasi dan member dari operasi tersebut
kesulitanOps={}     #menampung operasi dan tingkat kesulitannya
i=1                 #deklarasi variabel i yaitu variabel parameter untuk menjalankan input nama tentara berdasar jenis

tentara_berbeda=int(input())
while (True):
    #program input tentara berjalan jika i <= jumlah jenis tentara yang berbeda
    if i<=tentara_berbeda:
        while i<=tentara_berbeda:
            pisah_input=input().split()
            jumlahTentara=int(pisah_input[1])
            nama_jenis=pisah_input[0]
            JenisSoldier.add(nama_jenis)
            #memisahkan input dengan titik koma
            for j in range (jumlahTentara):
                IdentitasTentara = input().split(";")
                namaTentara=IdentitasTentara[0]
                umurTentara=IdentitasTentara[1]
                kekuatanTentara=IdentitasTentara[2]
                namasoldier.append(Tentara(nama_jenis, namaTentara, umurTentara, kekuatanTentara))
            i=i+1
    #apabila nilai i sudah lebih dari jumlah perbedaan tentara, lanjut ke program berikutnya
    else:
        perintah=input().split()
        if perintah[0]== "NEW":
            if perintah[1]=="TENTARA":
                #eksekusi bila input NEW TENTARA <jenis> <identitas>
                nama_jenis2=perintah[2]
                IdentitasTentara=perintah[3].split(";")
                namaTentara=IdentitasTentara[0]
                umurTentara=IdentitasTentara[1]
                kekuatanTentara=IdentitasTentara[2]
                #memasukkan identitas tentara yg menjadi sebuah object ke dalam namasoldier
                namasoldier.append(Tentara(nama_jenis2, namaTentara, umurTentara, kekuatanTentara))
                JenisSoldier.add(nama_jenis2)
                print(namaTentara+" bergabung")             
            elif perintah[1]=="OPERASI":
                #eksekusi bila input NEW OPERASI <nama operasi> <level>
                nama_ops=perintah[2]
                JenisOperasi[nama_ops]=[]
                levelKesulitan=int(perintah[3])
                kesulitanOps[nama_ops]=levelKesulitan
                print("Operasi "+perintah[2]+" dengan tingkat kesulitan",perintah[3]+" berhasil dibuat")
        elif perintah[0]=="MASUK":
            #eksekusi input MASUK
            #apabila jenis tentara tidak ada dalam list JenisSoldier
            if perintah[1] not in JenisSoldier:
                print("Tidak ada "+perintah[1])
            #apabila jenis tentara ada dalam list, di cek apakah ada nama tentara pada jenis tentara tersebut
            elif perintah[1] in JenisSoldier:
                ada=False
                for x in namasoldier:
                    if x.getNama() == perintah[2] and x.getJenis()== perintah[1]:
                        penampungNama=x
                        ada=True
                        break
                #apabila tidak ada nama tentara pada jenis tentara nya
                if not ada:
                    print("Tidak ada "+perintah[1]+" bernama "+perintah[2])
                #apabila operasi nya tidak ada
                elif perintah[3] not in JenisOperasi:
                    print("Tidak ada operasi "+perintah[3])
                #kemungkinan terakhir bila semua nya ada 
                else:
                    nama_ops=perintah[3]
                    #apabila nama yang dimasukkan ada di JenisOperasi pada key nama_ops
                    if penampungNama not in JenisOperasi[nama_ops]:
                        JenisOperasi[nama_ops].append(penampungNama)
                        print(perintah[2]+" masuk ke dalam tim operasi "+perintah[3])
                    #apabila nama yang dimasukkan tidak ada di JenisOperasi pada key nama_ops
                    else:
                        print(perintah[2]+" sudah ada di dalam tim operasi "+perintah[3])
        elif perintah[0]=="BERAKSI":
            nama_ops=perintah[2]
            #eksekusi perintah beraksi
            #apabila nama_ops tidak ada di JenisOperasi
            if nama_ops not in JenisOperasi:
                print("Tidak ada operasi "+nama_ops)
            #apabila ada
            else:
                sulit=kesulitanOps[nama_ops]    #mengakses data kesulitan operasi yang dipilih
                #apabila ada personil pada operasi
                if len(JenisOperasi[nama_ops]):
                    print ("Tim Operasi "+nama_ops+" beraksi, personil: ", end="")
                    x=1 #variabel increment. 
                    #perulangan untuk mengeprint nama tentara dalam operasi
                    for tentara in JenisOperasi[nama_ops]:
                        print(tentara.getNama(), end="")
                        #apabila x kurang dari jumlah data nama operasi pada jenis operasi
                        #nama tentara akan diprint
                        if x<len(JenisOperasi[nama_ops]):
                            print(',', end='')
                            x+=1
                        else:
                            print()
                        tentara.tambahLevel(sulit)
                    print("Level setiap personil bertambah ",sulit)
                #apabila tidak ada
                else:
                    print("Tidak ada personil pada tim operasi "+perintah[2])       
        elif perintah[0]=="KELUAR":
            nama_ops2=perintah[2]
            #apabila nama operasi tidak ada pada list jenis operasi
            if nama_ops2 not in JenisOperasi:
                print("Tidak ada operasi"+nama_ops2)
            else:
                #mengecek apabila nama tentara ada pada operasi
                ketemu=False
                for tentara in JenisOperasi[nama_ops2]:
                    #apabila nama tentara ada pada operasi maka nama tersebut diremove
                    if tentara.getNama()==perintah[1]:
                        JenisOperasi[nama_ops2].remove(tentara)
                        print(perintah[1]+" dikeluarkan dari tim operasi "+perintah[2])
                        ketemu=True
                #apabila tidak ada nama tentaranya
                if not ketemu:
                    print("Tidak ada tentara bernama"+perintah[1])
        elif perintah[0]=="PELATIHAN":
            #eksekusi perintah pelatihan
            if perintah[1] not in JenisSoldier:
                print("Tidak ada ",perintah[1])
            else: 
                print(perintah[1]+" melakukan pelatihan")
                #perulangan setiap tentara pada list namasoldier
                for tentara in namasoldier:
                    #apabila nama jenis tentara pada perintah 1 sama dengan object jenis maka akan bertambah 100 kekuatannya
                    if tentara.getJenis()== perintah[1]:
                        tentara.tambahKuat(100)
                        print("- Kekuatan "+tentara.getNama()+" bertambah menjadi ",tentara.getKuat())
        elif perintah[0]=="SUMMARY":
            #eksekusi perintah summary
            #apabila perintahnya SUMMARY ALL
            if perintah[1]=="ALL":
                for jenis in JenisSoldier:
                    print(jenis)
                    #meng print data tentara yang ada pada list namasoldier
                    for tentara in namasoldier:
                        if tentara.getJenis()==jenis:
                            print("- ", tentara)
            #apabila hanya SUMMARY saja perintahnya
            elif perintah[1]!="ALL":
                #apabila tidak ada jenis tentara yang diinginkan
                if perintah[1] not in JenisSoldier:
                    print("Tidak ada ",perintah[1])
                #apabila ada
                else:
                    #mencari tentara yang ingin dicari. apabila ditemukan maka akan diprint data nya
                    ketemu=False
                    for tentara in namasoldier:
                        if tentara.getNama() == perintah[2] and tentara.getJenis()==perintah[1]:
                            print(tentara)           
                            ketemu=True
                    #apabila nama tentara tidak ada pada namasoldier
                    if not ketemu:
                        print("Tidak ada "+perintah[1]+" dengan nama "+perintah[2])
        else:
            print("perintah salah!")
