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
print()
count=0
column=0
row=0
for r in grid:
    column=0
    for c in r:
        count=0
        if c==0:
            if column<4 and r[column+1]=='M':
                count+=1
            if column>1 and r[column-1]=='M':
                count+=1
            if row>0 and grid[row-1][column]=='M':
                count+=1
            if row<4 and grid[row+1][column]=='M':
                count+=1                
            r[column]=count
            
        column=column+1
    row+=1   
for r in grid:
    print(r)
            




