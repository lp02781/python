class NewClass():
    def __init__ (self,attribute='default', name='Instance'):
        self.name=name
        self.__attribute=attribute
    def __str__(self):
        return '{} has attribute {}'.format(self.name, self.__attribute)

    
