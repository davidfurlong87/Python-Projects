from random import randint
guesses=eval(input('how many guesses do you wanna take?'))
for i in range(guesses):
        x = randint(1, 10)
        guess=int(input('Whats your guess?'))
        if guess==x:
            print('wow! great job!')
        else:
            print('too bad')