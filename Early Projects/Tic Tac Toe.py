from random import randint
def tic():
    global l
    completed=False
    while completed==False:
        r=randint(0,2)
        c=randint(0,2)
        if l[r][c]==0:
            l[r][c]=2
            completed=True
    for r in l:
        print(r)
    print()
    print('x'*20)
    print()
    
l=[[0 for c in range(3)] for r in range(3)]
    
p_winner=False
c_winner=False
while p_winner==False or c_winner==False:
    r=eval(input('Please enter the row'))
    c=eval(input('Please enter the column'))
    l[r-1][c-1]=1
    for r in l:
        if r[0]==r[1]==r[2]==1:
            print('row winner')
            p_winner=True            
    for c in range(3):
        if l[0][c]==l[1][c]==l[2][c]==1:
            p_winner=True
    if l[0][0]==l[1][1]==l[2][2]==1:
        p_winner=True
    if l[0][2]==l[1][1]==l[2][0]==1:
        p_winner=True
    if p_winner==True:
        break
    
    
    tic()
    for r in l:
        if r.count(2)==3:
            c_winner=True
    for c in range(3):
        if l[0][c]==l[1][c]==l[2][c]==2:
            c_winner=True
    if l[0][0]==l[1][1]==l[2][2]==2:
        c_winner=True
    if l[0][2]==l[1][1]==l[2][0]==2:
        c_winner=True
    if c_winner==True:
        break
if p_winner==True:
    print('You are win!')
else:
    print('You are lsoe!')
for r in l:
        print(r)
        



