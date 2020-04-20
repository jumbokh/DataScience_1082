from animalClass2 import Animal, Lion, Duck, Sheep

def main():
    lionObj = Lion('Luke')
    print('Lion Object')
    print('Name: %s'%(lionObj.getName()))
    displayInform(lionObj)
    print()

    duckObj = Duck('Kiki')
    print('Duck object')
    print('Name: %s'%(duckObj.getName()))
    displayInform(duckObj)
    print()

    sheepObj = Sheep('Nala')
    print('sheep object')
    print('Name: %s'%(sheepObj.getName()))
    displayInform(sheepObj)
    print()
    
#Polymorphism
def displayInform(obj):    
    print('Breed: %s'%(obj.breed()))
    print('Food: %s'%(obj.food()))
    
main()