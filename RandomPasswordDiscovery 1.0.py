import random
import time

print('='*25)
print('RANDOM PASSWORD DISCOVERY')
print('='*25)

print('Select a difficult by typing a number between 1 and 4')
print('''[1] VERY EASY
[2] EASY
[3] MEDIUM
[4] HARD''')

pass1 = random.randint(0, 9)
pass2 = random.randint(0, 99)
pass3 = random.randint(0, 999)
pass4 = random.randint(0, 9999)
diff = int(input('Select difficult: '))
print('='*25)
while diff < 1 or diff > 4:
    print('You inserted an wrong number, please, select your difficult again')
    diff = int(input('Select difficult: '))
if diff == 1:
    print('Great! You choose the difficult \033[34mvery easy\033[m!')
elif diff == 2:
    print('Great! You choose the difficult \033[34measy\033[m!')
elif diff == 3:
    print('Great! You choose the difficult \033[34mmedium\033[m!')
elif diff == 4:
    print('Great! You choose the difficult \033[34mhard\033[m!')
    time.sleep(1)
    print('To make things harder, I will challenge you!')
    time.sleep(1)
    print('By now, you have only 10 tries!')
    time.sleep(1)
    print('Good luck!')
time.sleep(2)
print('GENERATING PASSWORD.')
time.sleep(1)
print('GENERATING PASSWORD..')
time.sleep(1)
print('GENERATING PASSWORD...')
time.sleep(1)
print('{:-^25}'.format(' STARTING '))
time.sleep(2)
if diff == 1:
    print(f'The password contain {diff} digit')
else:
    print(f'The password contain {diff} digits')

### VERY EASY MODE ###
if diff == 1:
    c = 0
    guess = -1
    while guess != pass1:
        c += 1
        guess = int(input('What your guess? '))
        if guess != pass1:
            print('Incorret!')
        else:
            break
        time.sleep(1)
        if c == 5:
            print('Let me try to help you!')
            if pass1 > 5:
                print('The password is higher than 5!')
            elif pass1 < 5:
                print('The password is lower than 5!')
            else:
                print('You getting closer, keep trying!')
    print(f'Congratulations! The password was {pass1}!')

### EASY MODE ###
if diff == 2:
    c = 0
    guess = -1
    while guess != pass2:
        c = c+1
        guess = int(input('What your guess? '))
        if c == 5:
            print('Let me try to help you!')
            if pass2 > 30:
                print('The password is higher than 30!')
            elif pass2 < 70:
                print('The password is lower than 70!')
            elif pass2 > 20 and pass2 < 60:
                print('The password is between 20 and 60!')
            else:
                print('You getting closer, keep trying!')
        if c == 10:
            print('Let me try to help you again!')
            if pass2 > 70:
                print('The password is higher than 70!')
            else:
                print('The password is lower than 70!')
        if c == 15:
            print('You getting closer, let me help you!')
        if c >= 15:
            if guess < pass2:
                print('HIGHER!')
            elif guess > pass2:
                print('LOWER')
        print('WRONG!')
    print(f'Congratulations! The password was {pass2}!')

### MEDIUM MODE ###
if diff == 3:
    c = 0
    guess = -1
    pass3tip = str(pass3)
    while guess != pass3:
        c += 1
        guess = int(input("What's your guess? "))
        if c >= 1:
            if guess < pass3:
                print('HIGHER')
            elif guess > pass3:
                print('LOWER')
        if c == 3:
            print(f'Let me try to help you!')
            time.sleep(1)
            print(f'The password contain 3 digits and the first one is {pass3tip[0]}')
        if c == 6:
            print(f'Let me try to help you again!')
            time.sleep(1)
            print(f'The first digit is {pass3tip[0]} and the second is {pass3tip[1]}')
    print(f'Congratulations! The password was {pass3}!')

### HARD MODE ###
if diff == 4:
    c = 10
    guess = -1
    while guess != pass4:
        c = c - 1
        guess = int(input('What your guess? '))
        if guess < pass4:
            print('HIGHER!')
        elif guess > pass4:
            print('LOWER')
        else:
            print(f'Congratulations! The password was {pass4}!')
            break
        if c == 0:
            print('Sorry, you lost! Good luck next time.')
            break
        elif c > 1:
            print(f'You still have {c} tries!')
        elif c == 1:
            print(f'Your last try!')
