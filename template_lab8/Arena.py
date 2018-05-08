from Daster import Daster

# input atribut Daster 1
print("Masukkan atribut Daster 1 ")
name1 = input("Nama Daster 1 \t\t\t: ")
HP1 = int(input("HP Daster 1 \t\t\t: "))
damage1 = int(input("Attack Damage Daster 1 \t\t: "))
heal1 = int(input("Heal Amount Daster 1 \t\t: "))
specialMoves1 = input("Nama Special Moves Daster 1 \t: ")
specialMovesDamage1 = int(input("Damage Special Moves Daster 1 \t: "))
specialMovesCooldown1 = int(input("Cooldown Special Moves Daster 1 : "))
elemen1 = input("Elemen Daster 1 \t\t: ")

print("----------------------------")
# input atribut Daster 2
print("Masukkan atribut Daster 2 ")
name2 = input("Nama Daster 2 \t\t\t: ")
HP2 = int(input("HP Daster 2 \t\t\t: "))
damage2 = int(input("Attack Damage Daster 2 \t\t: "))
heal2 = int(input("Heal Amount Daster 2 \t\t: "))
specialMoves2 = input("Nama Special Moves Daster 2 \t: ")
specialMovesDamage2 = int(input("Damage Special Moves Daster 2 \t: "))
specialMovesCooldown2 = int(input("Cooldown Special Moves Daster 2 : "))
elemen2 = input("Elemen Daster 2 \t\t: ")
print("----------------------------")
# instansiasi kedua Daster
daster1 = Daster(name1, HP1, damage1, heal1, specialMoves1, specialMovesDamage1, specialMovesCooldown1, elemen1)
daster2 = Daster(name2, HP2, damage2, heal2, specialMoves2, specialMovesDamage2, specialMovesCooldown2, elemen2)

counter = 0

# Pertarungan dimulai
while (daster1.HP>0 and daster2.HP>0):
    gantiGiliran = True

    # Giliran Daster 1
    if counter % 2 == 0:
        #input action Daster 1
        action = input("Giliran "+daster1.name+" : ")
        if action == 'ATTACK':
            # Daster 1 menyerang Daster 2
            daster1.attack(daster2)
            
        elif action == 'HEAL' :
            # Daster 1 menyembuhkan diri
            daster1.heal()
        elif action == 'SPECIAL MOVES':
            # Daster 1 menggunakan Special Moves
            gantiGiliran = daster1.useSpecialMoves(daster2)

    # Giliran Daster 2
    else :
        #input action Daster 2
        action = input("Giliran "+daster2.name+" : ")
        if action == 'ATTACK':
            # Daster 2 menyerang Daster 1
            daster2.attack(daster1)
        elif action == 'HEAL':
            # Daster 2 menyembuhkan diri
            daster2.heal()
        elif action == 'SPECIAL MOVES':
            # Daster 2 menggunakan Special Moves
            gantiGiliran = daster2.useSpecialMoves(daster1)
            
    if (gantiGiliran):
        counter+=1

# print pemenang pertarungan
if daster1.HP>0:
    pemenang=daster1
else:
    pemenang=daster2
print("Pemenangnya adalah {} dengan HP {}".format(pemenang.name,pemenang.HP))
