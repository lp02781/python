def komparator(x,y):
	if(x=='gunting'):
		if(y=='kertas'):
			return True
		elif(y=='batu'):
			return False
	elif(x=='kertas'):
		if(y=='batu'):
			return True
		elif(y=='gunting'):
			return False
	elif(x=='batu'):
		if(y=='gunting'):
			return True
		elif(y=='kertas'):
			return False
def score(x):
	
	global score1
	global score2
	
	for index in range(len(x)):
		if(x[index]==True):			
			score1+=1
		elif(x[index]==False):
			score2+=1

from datetime import datetime
def tanggal():
	return str(datetime.now())
while(True):
        try:
                score1=0
                score2=0
                player=[[],[]]
                player[0]=[]
                player[1]=[]
                namafile=input("")
                bacafile=open(namafile,'r')
                tulislog=open("Log permainan.txt",'a')
                tulislog.write(namafile)
                tulislog.write("\n")
                tulislog.write(tanggal())
                tulislog.write("\n")
                nomor=0
                for index in bacafile:
                        cache=index.split()
                        
                        player[nomor]=cache
                        nomor+=1
                        #player1=bacafile.readline().rstrip("\t\r\n").split(' ')
                        #player2=bacafile.readline().rstrip("\t\r\n").split(' ')
                bacafile.close()
                matches=[]
                for index in range(0,len(player[0])):
                        matches.append(komparator(player[0][index],player[1][index]))
                score(matches)
                print("Pemain pertama menang ",score1,"kali")
                print("Pemain pertama menang ",score1,"kali",file=tulislog)
                print("Pemain kedua menang ",score2,"kali")
                print("Pemain kedua menang ",score2,"kali",file=tulislog)
                if(score1<score2):
                        print("Hasil Permainan : Pemain kedua menang")
                        print("Hasil Permainan : Pemain kedua menang",file=tulislog)
                elif(score1>score2):
                        print("Hasil Permainan : Pemain pertama menang")
                        print("Hasil Permainan : Pemain pertama menang",file=tulislog)
                elif(score1==score2):
                        print("Hasil Permainan : imbang")
                        print("Hasil Permainan : imbang",file=tulislog)

                tulislog.write("\n")
                tulislog.close()
        except IOError:
                print("{:<0s} tidak ada filenya".format(namafile))
        except KeyboardInterrupt:
                
                break
        






