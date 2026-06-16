#import random for random generated number
import random

jackpot = random.randint(1,100)
guess = int(input('Guess the number between 1 and 100'))
counter = 1  # counter for counting the number of attempts

while guess != jackpot:
    if guess < jackpot:
        print('Guess higher')
    else:
        print('Guess lower')

    guess = int(input('Guess the number between 1 and 100: '))
    counter += 1

print('Congratulations — you guessed correctly!')
print('Attempts:', counter)
