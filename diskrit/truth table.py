def implies(a,b):
    if a:
        return b
    else:
        return True
print ('implies:\np \t  q\t p->q')

for p in [True, False]:
    for q in [True, False]:
        print (p,'\t',q,'\t',implies(p,q))
