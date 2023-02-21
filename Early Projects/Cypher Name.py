source = input('Enter your name: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
currentLetterPosition = 0
letterInAlphabet = ''
cypherName = ''
for i in range(len(source)):
    if source[i] == 'z':
        cypherName = cypherName + 'a'
    else:    
        currentLetterPosition = alphabet.index(source[i])
        cypherName = cypherName + alphabet[(currentLetterPosition + 1)]
print(cypherName)

#check this with z
    
