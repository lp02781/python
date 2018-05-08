digraph=[("a","a"),("a","b"),("b","c"),("b","d"),("c","d"),("c","e"),("d","b"),("d","c"),("e","a")]
angka_digraph = [(ord(a)-ord('a'),ord(b)-ord('b')) for (a,b) in digraph]
print(angka_digraph)

idx=0
while (idx<len(angka_digraph)):
    idx=0
    for isi in angka_digraph:
        for isi_2 in angka_digraph:
            if isi==isi_2:
                idx+=1
            elif (isi[1]==isi_2[0]) and (isi[0], isi_2[1]) not in angka_digraph:
                angka_digraph.append((isi[0],isi_2[1]))
            else:
                idx+=1

print(angka_digraph)
