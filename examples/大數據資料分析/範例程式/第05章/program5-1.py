import random
correct = random.randint(1, 100)
guess = eval(input('Guess a number: '))
while  True:
    if guess > correct:
        print(guess, '> correct')
    elif guess < correct:
        print(guess, '< correct')
    else:
        print('Correct number is ', correct)
        print('You got it')
        break
    guess = eval(input('Guess a number: '))