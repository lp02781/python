#PROGRAM TRENDING TOPIC DAN TOP MENTION
#GOLDY TANJUNG WIJAYA

import string
hashtag =[]                                 #list hashtag yang berfungsi sebagai penampung data yang didapat dari perhitungan
tes = string.punctuation
#fungsi perhitungan trending topic dan top mention
def perhitungan (tanda,limit):              #tanda adalah variabel untuk menentukan input adalah karakter # atau @. limit adalah variabel yang membatasi indeks 7 teratas utk trending topic dan 5 teratas utk top people
    bukafile = open(negara+".txt")          #membuka file belanda.txt, indonesia.txt, atau malaysia.txt sesuai input
    bacafile = bukafile.readlines()         #membaca file .txt tersebut per baris
    hastag =[]                              #list kosong untuk menyimpan nama-nama hashtag atau mention-an
    temp = []                               #list kosong untuk menampung sementara data dari list hastag, yang nantinya ditransfer pada list hashtag
    itung =[]                               #list kosong untuk menampung jumlah hashtag atau mention terbesar
    #perulangan agar proses pembacaan dilakukan sejumlah baris pada file
    for baris in bacafile:
        pisah = baris.split()               #memisahkan kata per kata dengan batasan spasi
        #perulangan agar proses pembacaan dilakukan sejumlah kata pada baris
        for kata in pisah:
            #perulangan agar nilai indeks sejumlah kata
            for idx in range (len(kata)):
                #mengeset dimulainya pembacaan setelah tanda # atau @
                if kata[idx]==tanda:
                    kata=kata[idx:]
                    break
            #apabila ada tanda # atau @ pada kata
            if tanda in kata:
                #mengecek apakah kata ada pada hastag
                if kata in hastag:
                    itung[hastag.index(kata)] +=1       #melakukan increment apabila ada kata yang sama
                else:   
                    hastag.append(kata)                 #memasukkan kata tersebut didalam list hastag
                    itung.append(1)                     #memulai perhitungan dari 1
    cpy_itung = itung[0:]                               #membuat copy dari list itung                     
    cpy_itung.sort(reverse=True)                        #membalik isi array cpy_itung
    #menampilkan hashtag dan mention-an yang adalah urutan 7 teratas
    for x in range (0,limit):
        indeks = itung.index(cpy_itung[x])
        print(hastag[indeks])
        temp.append(hastag[indeks])                     #memindahkan isi list hastag ke list temp
        itung[indeks]=0                                 #mereset indeks agar tidak mengecek elemen list yang sama lagi
    bukafile.close()                                    #menutup file
    hashtag.append(temp)                                #memasukkan list temp ke list hashtag

#input dari user
nama = input ("Masukkan Nama Anda: ")
negara = input ("Masukkan Negara Trending Topic: ")
negara = negara.lower()                                 #membuat input negara selalu huruf kecil
print("TOP 7 Trending")
perhitungan("#",7)                                      #memunculkan 7 trending topic dengan function perhitungan
print("5 TOP People")
perhitungan("@",5)                                      #memunculkan 5 top people dengan function perhitungan


#menulis pada file .html
result = open("tgs.html","w")
result.write("<!DOCTYPE html>\n")
result.write("<html>\n")
result.write("<head>\n")
result.write("<title>"+nama+" | Twitter Trending Simulation</title>\n") #nama berasal dari variabel nama yang diinput user
result.write("<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css\"> \n")
result.write("<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\"></script>\n")
result.write("<<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js\"></script>\n")
result.write("<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js\"></script>\n")
result.write("</head>\n")
result.write("<body>\n")
result.write("<h1 class=\"text-center\">7 Trending Topic</h1>\n")
result.write("<div class=\"container\">\n")
#dilakukan proses perulangan untuk menuliskan content
for i in range (0,7):
    #mengecek karakter terakhir pada hashtag apakah punctuation (tanda baca) atau bukan
    if hashtag[0][i][-1] in string.punctuation:                                 
        hashtag [0][i] = hashtag[0][i][0:len(hashtag[0][i])-1]                   #apabila karakter terakhir adalah punctuation, hashtag ditulis tidak dengan karakter terakhirnya
    link_hastag = "https://www.twitter.com/hashtag/"+str(hashtag[0][i][1:])      #digunakan 2 dimensional array dan slicing
    result.write("<a class=\"text-center\" href=\""+ str(link_hastag)+"\">"+str(hashtag[0][i])+"</a><hr>\n")    
result.write("</div>\n")
result.write("<h1 class=\"text-center\">5 Top People</h1>\n")
result.write("<div class=\"container\">\n")
#dilakukan proses perulangan untuk menuliskan content
for i in range (0,5):
    #mengecek karakter terakhir pada account apakah punctuation (tanda baca) atau bukan
    if hashtag[1][i][-1] in string.punctuation:
        hashtag [1][i] = hashtag[1][i][0:len(hashtag[1][i])-1]                  #apabila karakter terakhir adalah punctuation, hashtag ditulis tidak dengan karakter terakhirnya
    link_mention = "https://www.twitter.com/"+str(hashtag[1][i][1:])            #digunakan 2 dimensional array dan slicing
    result.write("<a class=\"text-center\" href=\""+str(link_mention)+"\">"+str(hashtag[1][i])+"</a><hr>\n") 
result.write("</div>\n")
result.write("</body>\n")
result.write("</html>\n")
result.close()       
