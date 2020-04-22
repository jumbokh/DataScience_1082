weight = eval(input('Enter your weight: '))
height = eval(input('Enter your height: '))
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