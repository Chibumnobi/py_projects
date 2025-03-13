import random
lives = 15
print('Welecome to nobi\'s Guessing game')
print(f'Lives left: {lives}')
num = random.randint(0, 101)
while lives != 0:
    guess = int(input('Pick a number from 1 to 100: '))
    if guess == num:
        m = int(input(('Congrats you got it! press 1 to play again or 2 to end')))
        if m == 1:
            num = random.randint(0, 101)
            lives = 15
            print(f'Lives left: {lives}')
        elif m == 2:
            print('Have a nice day')
            break
    elif guess < num:
        print('Your guess is lower than mine. Guess again!')
        lives -= 1
        print(f'Lives left: {lives}')
    elif guess > num:
        print('Your number is higher than mine. Guess again!')
        lives -= 1
        print(f'Lives left: {lives}')
    if lives == 0:
        g = int(input(('Sorry your out of lives. press 1 to end the game press 2 to play again')))
        if g == 1:
            print('Have a nice day')
            break
        elif g == 2:
            num = random.randint(0, 101)
            lives = 10
            print(f'Lives left: {lives}')
            continue
    else:
        continue