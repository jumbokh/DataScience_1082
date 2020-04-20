number = 0
set1 = 'Is your number in this set1? \n' + \
     ' 1,  3,  5,  7\n' + \
     ' 9, 11, 13, 15\n' + \
     '17, 19, 21, 23\n' + \
     '25, 27, 29, 31\n' + \
     '33, 35, 37, 39\n' + \
     '41, 43, 45, 47\n' + \
     '49\n' + \
     '\nEnter 0 for No and 1 for Yes: '
answer = eval(input(set1))
if answer == 1:
    number += 1

set2 = 'Is your number in this set2? \n' + \
     ' 2,  3,  6,  7\n' + \
     '10, 11, 14, 15\n' + \
     '18, 19, 22, 23\n' + \
     '26, 27, 30, 31\n' + \
     '34, 35, 38, 39\n' + \
     '42, 43, 46, 47\n' + \
     '50\n' + \
     '\nEnter 0 for No and 1 for Yes: '
answer = eval(input(set2))
if answer == 1:
    number += 2

set3 = 'Is your number in this set3? \n' + \
     ' 4,  5,  6,  7\n' + \
     '12, 13, 14, 15\n' + \
     '20, 21, 22, 23\n' + \
     '28, 29, 30, 31\n' + \
     '36, 37, 38, 39\n' + \
     '44, 45, 46, 47\n' + \
     '\nEnter 0 for No and 1 for Yes: '
answer = eval(input(set3))
if answer == 1:
    number += 4

set4 = 'Is your number in this set4? \n' + \
     ' 8,  9, 10, 11\n' + \
     '12, 13, 14, 15\n' + \
     '24, 25, 26, 27\n' + \
     '28, 29, 30, 31\n' + \
     '40, 41, 42, 43\n' + \
     '44, 45, 47\n' + \
     '\nEnter 0 for No and 1 for Yes: '
answer = eval(input(set4))
if answer == 1:
    number += 8

set5 = 'Is your number in this set5? \n' + \
     '16, 17, 18, 19\n' + \
     '20, 21, 22, 23\n' + \
     '24, 25, 26, 27\n' + \
     '28, 29, 30, 31\n' + \
     '48, 49, 50\n' + \
     '\nEnter 0 for No and 1 for Yes: '
answer = eval(input(set5))
if answer == 1:
    number += 16

set6 = 'Is your number in this set6? \n' + \
     '32, 33, 34, 35\n' + \
     '36, 37, 38, 39\n' + \
     '40, 41, 42, 43\n' + \
     '44, 45, 46, 47\n' + \
     '48, 49, 50\n' + \
     '\nEnter 0 for No and 1 for Yes: '
answer = eval(input(set6))
if answer == 1:
    number += 32
    
print('\nYour number is %d.'%(number))