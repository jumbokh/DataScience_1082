from animalClass import Animal, Lion, Duck
    
def main():
    lionObj = Lion('Luke')
    print('Lion Object')
    print('Name: %s'%(lionObj.getName()))
    print('Breed: %s'%(lionObj.breed()))
    print('Food: %s'%(lionObj.food()))
    print()

    duckObj = Duck('Kiki')
    print('Duck object')
    print('Name: %s'%(duckObj.getName()))
    print('Breed: %s'%(duckObj.breed()))
    print('Food: %s'%(duckObj.food()))

main()