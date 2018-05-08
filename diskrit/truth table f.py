def implikasi (c,d):
    if c==1 and d==1:
        return True
    else:
        return False
        
def implies(implikasi,c):
    if implikasi:
        return c
    else:
        return True
    
print ('implies:\np \t  q\t p\t(p^q)->p')


for p in [True, False]:
    for q in [True, False]:
            x = implies((implikasi(p,q)),p)
            print (p,'\t',q,'\t',p,'\t',x)
