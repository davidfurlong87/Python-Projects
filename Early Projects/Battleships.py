#basic battleships game to be played in shell

from random import randint

grid = [[randint(0,1) for c in range(5)] for r in range(5)]
masked_grid = [['x' for c in range(5)]for r in range(5)]

print('''Basic single-player battleships game.
Enter a row and column to check against an obscured grid.
When prompted, enter a number between 1 and 5 for each.
Get a score of 5 to win.
Good luck!''')

points=0
while points<5:
    print()
    for r in masked_grid:
        print(r)
    x = 0
    y = 0
    x = eval(input('Please enter the row (1 - 5): '))
    if str(x) not in '12345':
        continue
    y = eval(input('Please enter the column (1 - 5): '))
    if str(y) not in '12345':
        continue
    print()
    if grid[x-1][y-1]==1:
        print('Hit!')
        points=points+1
        masked_grid[x-1][y-1] = '0'
    else:
        print('Miss!')

print('Congratulations')
        
