def append_tuple(tuple_utama, x):
    tuple_utama += (x,)
    return tuple_utama

n = int(input(""))
key = ()
key_nama = ()

for index in range(n):
    kunci = input("").split()
    kun_ci = (kunci[1],kunci[2])
    key = append_tuple(key, kun_ci)
    key_nama+=(kunci[0],)

login = input("").split()
login = tuple(login)

if login in key:
    print('Hallo',key_nama[key.index(login)])
else:
    print('gagal login')

