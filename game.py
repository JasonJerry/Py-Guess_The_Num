
from random import randint

computer = randint(0, 10)

print('Hi! I just thought on a number beteween 0 and 10. Can you guess what number did i think?')

hit = False

guess = 0

while not hit:

    player = int(input('What is your guess? '))

    guess += 1

    if player == computer:

        hit = True

    else:

        if player < computer:

            print('konjam mela(UP)')

        elif player > computer:

            print('konjam keela(DOWN)')

print(' You did it! Found the right answer with {} attempts'.format(guess))
