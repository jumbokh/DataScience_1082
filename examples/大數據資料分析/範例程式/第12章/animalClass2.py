class Animal:
    def __init__(self, name = 'Unknown'):
        self.__name = name

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'viviparous'

    def food(self):
        return 'meat'
    
class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'Oviparous'

    def food(self):
        return 'grass'