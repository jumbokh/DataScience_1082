def bmi(weight, height):
    heightMeter = height / 100
    bmi = weight / (heightMeter * heightMeter)
    print('Your bmi is %.2f'%(bmi))
    if bmi < 18.5:
        print('Underweight')
    elif bmi < 25:
        print('Normal')
    elif bmi < 30:
        print('Overweight')
    else:
        print('Obses')

def main():
    weight = eval(input('Enter your weight: '))

    height = eval(input('Enter your height: '))
    while weight > 0 and weight > 0:
        bmi(weight, height)
        weight = eval(input('Enter your weight: '))

        height = eval(input('Enter your height: '))
        
main()