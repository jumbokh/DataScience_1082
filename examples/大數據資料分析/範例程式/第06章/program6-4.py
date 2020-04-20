def gpa(score):
    if score >= 80:
        print('Your GPA is A.')
    elif score >= 70:
        print('Your GPA is B.')
    elif score >= 60:
        print('Your GPA is C.')
    elif score >= 50:
        print('Your GPA is D.')
    else:
        print('Your GPA is E.')

def main():
    score = eval(input('Enter your score: '))

    while score >= 0:
        gpa(score)
        score = eval(input('Enter your score: '))
        
main()