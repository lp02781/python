def implikasi (c,d):
    if c==1 and d==1:
        return True
    else:
        return False
        
def implies(implikasi,x):
    if implikasi:
        return x
    else:
        return True
    
print ('implies:\np \t  q\t r\t(p^q)->r')


for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            x = implies((implikasi(p,q)),r)
            print (p,'\t',q,'\t',r,'\t',x)
