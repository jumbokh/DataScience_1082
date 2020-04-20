class Bmi:
    def __init__(self, weight = 170, height = 60):
        self.__weight = weight
        self.__height = height
        
    def getBmi(self):
        heightMeter = self.__height / 100
        bmi = self.__weight / (heightMeter * heightMeter)
        print('%.2f'%(bmi))
        if bmi < 18.5:
            print('Underweight')
        elif bmi < 25:
            print('Normal')
        elif bmi < 30:
            print('Overweight')
        else:
            print('Obses')

def main():
    John = Bmi(68, 185)
    print('John\'s BMI is : ', end = '')
    John.getBmi()
    print()

    Mary = Bmi(53, 172)
    print('Mary\'s BMI is : ', end = '')
    Mary.getBmi()
    print()

main()