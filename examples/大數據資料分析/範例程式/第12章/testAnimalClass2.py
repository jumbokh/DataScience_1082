from animalClass import Animal, Lion, Duck

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
    
#Polymorphism
def displayInform(obj):    
    print('Breed: %s'%(obj.breed()))
    print('Food: %s'%(obj.food()))
    
main()