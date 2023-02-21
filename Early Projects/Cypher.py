alphabet = 'abcdefghijklmnopqrstuvwxyz'
qwerty = 'qwertyuiopasdfghjklzxcvbnm'
secretMessage = input('Whats your secret message: ')
for i in secretMessage:
    if i.isalpha():
        print(qwerty[alphabet.index(i)], end='')
    else:
        print(i, end='')