class Tentara:
    #inisialisasi tentara
    def __init__(self,nama,umur,kekuatan):
        self.nama=nama
        self.kekuatan=int(kekuatan)
        self.umur=umur
        self.level=int(1)

    def tambahkekuatan(self,kekuatan):
        self.kekuatan+=int(kekuatan)

    def tambahlevel(self,kesulitan):
        self.level+=int(kesulitan)

        
class Operasi:
    #inisialisasi operasi
    def __init__(self,namaoperasi,kesulitan):
        self.namaoperasi=namaoperasi
        self.kesulitan=int(kesulitan)
        self.tim=[]

operasi={}      #Menyimpan daftar operasi yang ada beserta objeknya
jenistentara={} #Menyimpan jenis tentara beserta daftar tentaranya
N=int(input('Banyak jenis tentara: '))
for i in range(0,N):
    masukan=input('')
    pisah=masukan.split()
    jenis=pisah[0]
    if jenis not in jenistentara:
        jenistentara[jenis]=[]
    M=int(pisah[1])
    for j in range(0,M):
        masukan1=input('')
        nama=masukan1.split(';')[0]
        umur=masukan1.split(';')[1]
        kekuatan=masukan1.split(';')[2]
        jenistentara[jenis].append(Tentara(nama,umur,kekuatan))

while True:
    masukan2=input('')
    pisah2=masukan2.split()

    #Perintah NEW
    if pisah2[0]=='NEW':
        #NEW TENTARA <Jenis> <nama;umur;kekuatan>
        if pisah2[1]=='TENTARA':
            jenis2=pisah2[2]
            detil=pisah2[3]
            nama=detil.split(';')[0]
            umur=detil.split(';')[1]
            kekuatan=detil.split(';')[2]
            if jenis2 not in jenistentara:
                jenistentara[jenis2]=[]
            jenistentara[jenis2].append(Tentara(nama,umur,kekuatan))
            print(nama+' bergabung')

        #NEW OPERASI <namaoperasi> <kesulitan>
        elif pisah2[1]=='OPERASI':
            namaoperasi=pisah2[2]
            kesulitan=pisah2[3]
            #Belum ada operasi
            if namaoperasi not in operasi:
                operasi[namaoperasi]=Operasi(namaoperasi,kesulitan)
                print('Operasi '+namaoperasi+' dengan tingkat kesulitan '+str(kesulitan)+' berhasil dibuat')
            #Operasi sudah ada
            else:
                print('Operasi '+namaoperasi+' sudah ada')
    #Perintah MASUK <jenis> <Namatentara> <Namaoperasi>
    elif pisah2[0]=='MASUK':
        jenis=pisah2[1]
        namatentara=pisah2[2]
        namaoperasi=pisah2[3]
        
        #Jenis tentara tidak ada
        if jenis not in jenistentara: 
            print('Tidak ada '+jenis)

        #Jenis tentara ada
        else:
            #Mencari nama tentara
            ketemu=0
            for i in range (0,len(jenistentara[jenis])):
                #nama tentara ditemukan
                if jenistentara[jenis][i].nama==namatentara:
                    ketemu=1
                    #Nama operasi ditemukan
                    if namaoperasi in operasi:
                        #Tentara sudah ada di tim operasi
                        if namatentara in operasi[namaoperasi].tim:
                            print(namatentara+' sudah ada di dalam tim operasi '+namaoperasi)
                        #Tentara belum ada di tim operasi
                        else:
                            operasi[namaoperasi].tim.append(namatentara)
                            print(namatentara+' masuk ke dalam tim operasi '+namaoperasi)
                    #Tidak ada operasi
                    else:
                        print('Tidak ada operasi bernama '+namaoperasi)
            #Tentara tidak ditemukan
            if ketemu!=1:
                print('Tidak ada '+jenis+' bernama '+namatentara)
    #Perintah KELUAR <NamaTentara> <NamaOperasi>
    elif pisah2[0]=='KELUAR':
        namatentara=pisah2[1]
        namaoperasi=pisah2[2]
        #Operasi tidak ada
        if namaoperasi not in operasi:
            print('Tidak ada operasi bernama '+namaoperasi)
        #Operasi ada
        else:
            #Tentara tidak ada
            if namatentara not in operasi[namaoperasi].tim:
                print('Tidak ada tentara bernama '+namatentara+' pada tim operasi '+namaoperasi)
            #Tentara ada kemudian dikeluarkan
            else:
                operasi[namaoperasi].tim.remove(namatentara)
                print(namatentara+' dikeluarkan dari tim operasi '+namaoperasi)
    #Perintah PELATIHAN <Jenis>
    elif pisah2[0]=='PELATIHAN':
        jenis=pisah2[1]
        #Jenis tentara tidak ada
        if jenis not in jenistentara:
            print('Tidak ada '+ jenis)
        #Jenis tentara ada
        else:
            print(jenis+' melakukan pelatihan')
            for i in range(0,len(jenistentara[jenis])):
                jenistentara[jenis][i].tambahkekuatan(100)    #Menambah kekuatan tentara sebesar 100
                print('- Kekuatan '+jenistentara[jenis][i].nama+' bertambah menjadi '+str(jenistentara[jenis][i].kekuatan))
    #Perintah BERAKSI OPERASI <NamaOperasi>
    elif pisah2[0]=='BERAKSI':
        namaoperasi=pisah2[2]
        #Tidak ada operasi
        if namaoperasi not in operasi:
            print('Tidak ada operasi '+namaoperasi)
        #Ada operasi
        else:
            #Tim operasi kosong            
            if len(operasi[namaoperasi].tim)==0:
                print('Tidak ada personil pada tim operasi '+namaoperasi)
            #Tim operasi ada
            else:
                #Mencetak operasi beserta personilnya
                print('Tim operasi '+namaoperasi+' beraksi, personil: ',end='')
                for i in range (0,len(operasi[namaoperasi].tim)):
                    print(operasi[namaoperasi].tim[i],end='')
                    if i!=len(operasi[namaoperasi].tim)-1:
                        print(', ',end='')
                    #menambah level tentara
                    for jenis in jenistentara:
                        for j in range (0,len(jenistentara[jenis])):
                            #Mencari tentara yang ikut beraksi
                            if jenistentara[jenis][j].nama==operasi[namaoperasi].tim[i]:
                                jenistentara[jenis][j].tambahlevel(operasi[namaoperasi].kesulitan)
                print('\nLevel setiap personil bertambah '+str(operasi[namaoperasi].kesulitan))
    #Perintah SUMMARY
    elif pisah2[0]=='SUMMARY':
        #Perintah SUMMARY ALL
        if pisah2[1]=='ALL':
            #Looping untuk mencetak semua daftar tentara
            for jenis in jenistentara:
                print(jenis)
                for i in range(0,len(jenistentara[jenis])):
                    print('- '+jenistentara[jenis][i].nama+' '+str(jenistentara[jenis][i].umur)+' tahun, kekuatan: '+str(jenistentara[jenis][i].kekuatan)+', level: '+str(jenistentara[jenis][i].level))
                    
        #Perintah SUMMARY <Jenis> <Namatentara>
        else:
            jenis=pisah2[1]
            namatentara=pisah2[2]
            #Jenis tentara ada
            if jenis in jenistentara:
                #Mencari nama tentara
                ketemu=0
                for i in range (0,len(jenistentara[jenis])):
                    #nama tentara ditemukan
                    if jenistentara[jenis][i].nama==namatentara:
                        ketemu=1
                #Nama tentara ditemukan
                if ketemu==1:
                    for i in range(0,len(jenistentara[jenis])):
                        if namatentara==jenistentara[jenis][i].nama:
                            print(namatentara+' '+str(jenistentara[jenis][i].umur)+' tahun, kekuatan: '+str(jenistentara[jenis][i].kekuatan)+', level: '+str(jenistentara[jenis][i].level))
                #Nama tentara tidak ditemukan
                else:
                    print('Tidak ada '+jenis+' dengan nama '+namatentara)
            #Jenis tentara tidak ada
            else:
                print('Tidak ada '+jenis)
                            
