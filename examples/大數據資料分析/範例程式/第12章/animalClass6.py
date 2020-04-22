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

    def sound(self):
        return 'hon-hon-hon'
    
class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'Oviparous'

    def food(self):
        return 'earthworm'

    def sound(self):
        return 'A-A-A'
    
class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'viviparous'

    def food(self):
        return 'grass'

    def sound(self):
        return 'Bei-Bei-Bei'