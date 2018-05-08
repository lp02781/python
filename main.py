from Soldier import *

# List of object of Soldier created
soldiers = []

# Set of specialist
specialists = set()

# Operation Name as the key
operationDifficulties = {} # Operation difficulties as the value
operationMembers = {} # Operation members as the value

numberOfSpecialist = int(input('Number of Soldiers : '))

# Create n number of specialists
for i in range(numberOfSpecialist):
    # Input format : <specialist type> <number of members>
    temp = input()
    temp = temp.split()

    specialists.add(temp[0])

    # Create n number of specialists' members
    for i in range(int(temp[1])):
        # Input format : <name of soldier>;<age>;<strength>
        soldierInfo = input()
        soldierInfo = soldierInfo.split(';')
        # Create the soldier
        soldiers.append(Soldier(temp[0], soldierInfo[0], soldierInfo[1], soldierInfo[2]))
print(soldiers)
print(specialists)

while(True):
    # Possible userInput : NEW, MASUK, KELUAR, PELATIHAN, BERAKSI, SUMMARY
    userInput = input('')
    userInput = userInput.split()

    # NEW format :
    # 1. NEW TENTARA <JenisTentara> <NamaTentara>;<Umur>;<Kekuatan>
    # 2. NEW OPERASI <NamaOperasi> <TingkatKesulitan>
    if userInput[0].title() == 'New':
        # Create a new soldier and append the 'soldiers' list with new created soldier
        if userInput[1].title() == 'Tentara':
            specialist = userInput[2]
            info = userInput[3].split(';')
            soldierName = info[0]
            soldierAge = info[1]
            soldierStrength = info[2]

            soldiers.append(Soldier(specialist, soldierName, soldierAge, soldierStrength))
            specialists.add(specialist)

            print('{} bergabung'.format(soldierName))

        # Create a new operation by appending the operationMembers and operationDifficulties dictionary
        elif userInput[1].title() == 'Operasi':
            operationName = userInput[2]
            difficulties = userInput[3]

            operationDifficulties[operationName] = difficulties
            operationMembers[operationName] = []

            print('Operasi {} dengan tingkat kesulitan {} berhasil dibuat'.format(operationName, difficulties))

        else:
            print('Wrong format.')
    
    # MASUK format :
    # MASUK <JenisTentara> <NamaTentara> <NamaOperasi>
    elif userInput[0].title() == 'Masuk':
        # Search the corresponding soldier in 'soldiers' list
        # Appending the list of 'operationMembers[namaoperasi]'
        specialist = userInput[1]
        soldierName = userInput[2]
        operationName = userInput[3]

        # If the specialist does not exist
        if specialist not in specialists:
            print('Tidak ada {}'.format(specialist))
        
        # If the specialist does exist, but there is no member such as in the input
        elif specialist in specialists:
            exist = False
            for soldier in soldiers:
                if soldier.getName() == soldierName and soldier.getSpecialist() == specialist:
                    tersangka = soldier
                    exist = True
                    break

            if not exist:
                print('Tidak ada {} bernama {}'.format(specialist, soldierName))
        
            # If the specialist does exits, the member in the input exist, but there's no such operation
            elif operationName not in operationMembers:
                print('Tidak ada operasi bernama {}'.format(operationName))
            
            # If the specialist does exist, the member in the input exists, and the operation exists
            else:
                # 2 possible conditions : the soldier not yet in the operation and the soldier already in the operation
                if tersangka not in operationMembers[operationName]:
                    operationMembers[operationName].append(tersangka)
                    print('{} masuk ke dalam tim operasi {}'.format(soldierName, operationName))
                
                else:
                    print('{} sudah ada di dalam tim operasi {}'.format(soldierName, operationName))

    # KELUAR format :
    # KELUAR <NamaTentara> <NamaOperasi>
    elif userInput[0].title() == 'Keluar':
        # Find the corresponding soldier in 'operationMembers[namaoperasi]'
        # Remove it
        soldierName = userInput[1]
        operationName = userInput[2]

        if operationName not in operationMembers:
            print('Tidak ada operasi bernama {}'.format(operationName))
        
        else:
            found = False
            # Try to find the corresponding soldier
            for soldier in operationMembers[operationName]:
                if soldier.getName() == soldierName:
                    operationMembers[operationName].remove(soldier)
                    print('{} dikeluarkan dari tim operasi {}'.format(soldierName, operationName))

                    found = True
            
            # If the corresponding soldier not found in the operation
            if not found:
                print('Tidak ada tentara bernama {} pada tim operasi {}'.format(soldierName, operationName))
    
    # PELATIHAN format :
    # PELATIHAN <JenisTentara>
    elif userInput[0].title() == 'Pelatihan':
        # All soldier with certain specialist type will gain power by 100
        specialist = userInput[1]

        # If specialist do not exist
        if specialist not in specialists:
            print('Tidak ada {}'.format(specialist))
        
        # If specialist does exist
        else:
            print('{} melakukan pelatihan'.format(specialist))
            for soldier in soldiers :
                if soldier.getSpecialist() == specialist:
                    soldier.gainStrength(100)
                    print('- Kekuatan {} bertambah menjadi {}'.format(soldier.getName(), soldier.getStrength()))
        
    # BERAKSI format :
    # BERAKSI OPERASI <namaOperasi>
    elif userInput[0].title() == 'Beraksi':
        # All soldier in that operation will gain level by the operation's difficulties
        operationName = userInput[2]

        # If operation do not exist
        if operationName not in operationMembers:
            print('Tidak ada operasi {}'.format(operationName))
        
        # If operation does exist
        else:
            difficulties = operationDifficulties[operationName]
            
            # There are members in the operation
            if len(operationMembers[operationName]):
                print('Tim operasi {} beraksi, personil : '.format(operationName), end = '')
                
                # Print the right format. i for counter so it prints the necessary ','
                i = 1
                for soldier in operationMembers[operationName]:
                    print(soldier.getName(), end = '')
                    if i < len(operationMembers[operationName]):
                        print(', ', end='')
                        i += 1
                    else:
                        print()
                    soldier.levelUP(difficulties)
                print('Level setiap personil bertambah {}'.format(difficulties))

            # No members in the operation
            else:
                print('Tidak ada personil pada tim operasi {}'.format(operationName))
    
    # SUMMAR format :
    # 1. SUMMARY <JenisTentara> <NamaTentara>
    # 2. SUMMARY ALL
    elif userInput[0].title() == 'Summary':
        if userInput[1].title() != 'All':
            # Find the corresponding soldier in 'soldiers' list and print it
            specialist = userInput[1]
            soldierName = userInput[2]

            # specialist does not exist
            if specialist not in specialists:
                print('Tidak ada {}'.format(specialist))
            
            # specialist does exist
            else:
                found = False
                # Try to find the corresponding soldier
                for soldier in soldiers:
                    if soldier.getName() == soldierName and soldier.getSpecialist() == specialist:
                        print(soldier)
                        found = True
                
                # Corrresponding soldier not found
                if not found:
                    print('Tidak ada {} dengan nama {}'.format(specialist, soldierName))
        
        elif userInput[1].title() == 'All':
            # Print all soldier in 'soldiers' list info
            for specialist in specialists:
                print('{:<15} :'.format(specialist))
                for soldier in soldiers:
                    if soldier.getSpecialist() == specialist:
                        print('- ', end='')
                        print(soldier)
            
        else :
            print('Wrong Format.')
    
    else :
        print('Perintah {} tidak ditemukan'.format(userInput[0]))
'''
Input nama dibatas (a-z)(A-Z)(0-9)
PENGHENTIAN PROGRAM DIATUR
'''
