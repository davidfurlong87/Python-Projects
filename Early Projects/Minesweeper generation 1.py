from random import randint
number_of_mines=0
while number_of_mines==0:
    number_of_mines=eval(input('How many mines do you want? (Min-1, Max-15)'))
    if number_of_mines==0 or number_of_mines>15:
        print('Error!')
        number_of_mines=0
        continue
grid=[['x' for i in range(5)] for i in range(5)]
m_count=0
changed_count=0
while changed_count<25:
    x= randint(0,4)
    y=randint(0,4)
    if grid[x][y]=='x':
        if m_count<number_of_mines:
            grid[x][y]='M'
            changed_count+=1
            m_count+=1
        else:
            grid[x][y]=0
            changed_count+=1
for r in grid:
    print(r)

