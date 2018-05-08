class Soldier():
    def __init__(self, specialist, name, age, strength):
        # Check the character so it contains only alphabet and number
        for char in name:
            # Take and compare ASCII number
            # 1-9 : (48-57) ; A-Z : (65-90) ; a-z : (97-122)
            char = ord(char)
            if char < 48 or 57 < char < 65 or 90 < char < 97 or char > 122 :
                print(':::Only accepts A-Z a-z 0-9. Object not created.:::')
                return None
        
        self.__specialist = specialist
        self.__name = name
        self.__age = int(age)
        self.__strength = int(strength)
        # Default level
        self.__level = 1
    
    def __str__(self):
        return '{} {} tahun, kekuatan : {}, level : {}'.format(self.__name, self.__age, self.__strength, self.__level)
    
    def getName(self):
        return self.__name
    
    def getSpecialist(self):
        return self.__specialist

    def getStrength(self):
        return self.__strength
    
    def gainStrength(self, value):
        self.__strength += int(value)
    
    def levelUP(self, value):
        self.__level += int(value)