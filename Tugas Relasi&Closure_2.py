A = [i for i in range(0,10)]
def Refleksif_closure(Set, relation):
    refleksi=[(i,i) for i in Set]
    closure=[isi for isi in relation]
    for isi in refleksi:
        if isi in closure:
            continue
        else:
            closure.append(isi)
    closure.sort()
    return closure

def Simetris_closure(Set, relation):
    simetris = [(a,b) for (b,a) in relation]
    closure = [isi for isi in relation]
    for isi in simetris:
        if isi in closure:
            continue
        else:
            for idx in range (len(closure)):
                if (isi[0]==closure[idx][1]) and (isi[1]==closure[idx][0]):
                    closure.insert(idx+1,isi)
    return closure

print(Refleksif_closure(A,[(0,1),(3,2),(6,8),(8,7),(5,9)]))
print(Simetris_closure(A,[(0,1),(3,2),(6,8),(8,7),(5,9)]))
