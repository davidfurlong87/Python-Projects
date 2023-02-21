from random import randint
import math
secret = input('Please enter the message to encrypt: ')
secret = secret.lower()
alpha = 'abcdefghijklmnopqrstuvwxyz'
l = []
lCy = []
lCyDe = []
x = ''
yRand = 0
z = 0
lCypherMemory = []
for i in range(len(secret)):
    l.append(secret[i])
for i in range(len(l)):
    #print('The current letter is:', secret[i])
    x = alpha.index(secret[i])
    #print('The index of this within alpha is:', x)
    yRand = randint(1, 26)
    lCypherMemory.append(yRand)
    if (x + yRand) > 26:
        z = (x + yRand) - 26
        lCy.append(alpha[z])
    else:
        lCy.append(alpha[x + yRand])
print('The Original decrypted message was:', l)
print('The encrypted message is:', lCy)
print('The cypher key is:', lCypherMemory)
for i in range(len(lCy)):
    if (alpha.index(lCy[i])) - lCypherMemory[i]<0:
        z = ((alpha.index(lCy[i])) - lCypherMemory[i]) + 26
        lCyDe.append(alpha[z])
    else:
        z = ((alpha.index(lCy[i])) - lCypherMemory[i])
        lCyDe.append(alpha[z])
print('The message decrypted is:', lCyDe)
        