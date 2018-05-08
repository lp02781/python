import Kalkulator #mengimport fungsi dari file Kalkulator.py

#Dictionary yang berisi harga per inchi kuadrat (disingkat hpik) untuk tiap makanan
#Jangan diubah
hpik = {"pizza":1000, "martabak":800, "mendoan":400}

#Gunakan fungsi yang telah Anda buat pada file Kalkulator.py

#fungsi untuk pembelian pizza
def beli_pizza(pembeli, ukuran, bentuk):
    #TODO Implementasikan fungsi yang mencetak keluaran seperti yang diinginkan
    #dan mengembalikan harga dari pizza yang dipesan
    print(pembeli, "membeli pizza berbentuk", bentuk, "dengan ukuran", ukuran, "inchi") #menampilkan output keterangan apa yang dibeli pelanggan
    hargapizza = hpik["pizza"]                                                          #menampilkan harga pizza dari dictionary
    #jika kondisi pizza yang dipesan bulat
    if bentuk == "bulat":
        luas = Kalkulator.luas_lingkaran(ukuran)
        harga_asli = hargapizza*luas            
        #jika ukuran prima, perhitungan harga nya seperti ini
        if Kalkulator.isPrima(ukuran) == True:
            harga_final1 = Kalkulator.harga_diskon(harga_asli, ukuran)
            return harga_final1
        #jika ukuran bukan prima
        else:
            return harga_asli
    #jika kondisi pizza yang dipesan persegi
    elif bentuk == "persegi":
        luas = Kalkulator.luas_persegi(ukuran)
        harga_asli = hargapizza*luas
        #jika ukuran prima, perhitungan harga nya seperti ini
        if Kalkulator.isPrima(ukuran) == True:
            harga_final1 = Kalkulator.harga_diskon(harga_asli, ukuran)
            return harga_final1
        #jika ukuran bukan prima
        else:
            return harga_asli

#fungsi untuk pembelian martabak
def beli_martabak(pembeli, ukuran, bentuk):
    #TODO Implementasikan fungsi yang mencetak keluaran seperti yang diinginkan
    #dan mengembalikan harga dari martabak yang dipesan
    print(pembeli, "membeli martabak berbentuk", bentuk, "dengan ukuran", ukuran, "inchi")  #menampilkan output keterangan apa yang dibeli pelanggan
    hargamartabak = hpik["martabak"]                                                        #menampilkan harga martabak dari dictionary
    #jika kondisi martabak yang dipesan bulat
    if bentuk == "bulat":
        luas = Kalkulator.luas_lingkaran(ukuran)
        harga_asli = hargamartabak*luas
        #jika ukuran prima, perhitungan harga nya seperti ini
        if Kalkulator.isPrima(ukuran) == True:
            harga_final2 = Kalkulator.harga_diskon(harga_asli, ukuran)
            return harga_final2
        #jika ukuran bukan prima
        else:
            return harga_asli
    #jika kondisi martabak yang dipesan persegi
    elif bentuk == "persegi":
        luas = Kalkulator.luas_persegi(ukuran)
        harga_asli = hargamartabak*luas
        #jika ukuran prima, perhitungan harga nya seperti ini
        if Kalkulator.isPrima(ukuran) == True:
            harga_final2 = Kalkulator.harga_diskon(harga_asli, ukuran)
            return harga_final2
        #jika ukuran bukan prima
        else:
            return harga_asli
    
def beli_mendoan(pembeli, ukuran, bentuk):
    #TODO Implementasikan fungsi yang mencetak keluaran seperti yang diinginkan
    #dan mengembalikan harga dari mendoan yang dipesan
    print(pembeli, "membeli mendoan berbentuk", bentuk, "dengan ukuran", ukuran, "inchi") #menampilkan output keterangan apa yang dibeli pelanggan
    hargamendoan = hpik["mendoan"]              #menampilkan harga mendoan dari dictionary
    #jika kondisi mendoan yang dipesan bulat
    if bentuk == "bulat":
        luas = Kalkulator.luas_lingkaran(ukuran)
        harga_asli = hargamendoan*luas
        #jika ukuran prima, perhitungan harga nya seperti ini
        if Kalkulator.isPrima(ukuran) == True:
            harga_final3 = Kalkulator.harga_diskon(harga_asli, ukuran)
            return harga_final3
        else:
            return harga_asli
    #jika kondisi mendoan yang dipesan persegi
    elif bentuk == "persegi":
        luas = Kalkulator.luas_persegi(ukuran)
        harga_asli = hargamendoan*luas
        #jika ukuran prima, perhitungan harga nya seperti ini
        if Kalkulator.isPrima(ukuran) == True:
            harga_final3 = Kalkulator.harga_diskon(harga_asli, ukuran)
            return harga_final3
        #jika ukuran bukan prima
        else:
            return harga_asli
    
    
def cetak(pembeli, harga_total):
    #TODO Implementasikan fungsi yang mencetak harga total seperti yang diinginkan
    print(pembeli, "selesai belanja, total harga:" , str(int(harga_total)))
