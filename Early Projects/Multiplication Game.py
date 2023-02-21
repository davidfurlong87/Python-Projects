from random import randint
cor = 0
incor = 0
for i in range (10):
    x1 = randint (1, 6)
    x2 = randint (1, 6)
    z = x1*x2
    print('What is the product of', x1, 'and', x2, '?')
    answer=eval(input())
    if answer==z:
        print('Correct!')
        cor=cor+1
    else:
        incor=incor+1
if cor<=2:
    print('Your number of correct answers was:', cor, 'this is very disappointing.')
elif cor>=3 and cor<=5:
    print('Your number of correct answers was:', cor, 'this is not so good.')
elif cor>=6 and cor<=8:
    print('Your number of correct answers was:', cor, 'this is pretty good.')
else:
    print('Your number of correct answers was:', cor, 'this is awesome!')