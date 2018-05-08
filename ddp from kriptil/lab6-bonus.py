import random
angka_ai = random.randrange(1,10)
deret = input("").split()
for index in range(len(deret)):
    deret[index] = int(deret[index])
deret = tuple(deret)
print("Bilangan Random:",angka_ai)
for angka in deret:
    if (angka % angka_ai == 0):
        print(angka,end=' ')
