print('How many players would you like?')
noOfPlayers = int(input('Well, what is it? '))
currentPlayer = 1
for i in range(noOfPlayers):
    print('The current player is', currentPlayer, i+1)
    currentPlayer = (currentPlayer%noOfPlayers)+1