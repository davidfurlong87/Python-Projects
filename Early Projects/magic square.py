from random import randint
rows=False
columns=False
count=0
while rows==False or columns==False:
    rows=False
    columns=False
    l = [[randint(1,2) for c in range(4)] for r in range(4)]
    for i in l:
        print(i)
    x = [sum(i) for i in l]
    #print(x)
    if x.count(x[0])!=4:
        print('Rows dont add up')
        count=count+1
        continue
    else:
        rows=True
    y = []    
    for c in range(4):
        y.append([])
        for r in range(4):
            y[c].append(l[r][c])
    #print(y)
    y2 = [sum(y[i]) for i in range(4)]
    #print(y2)
    if y2.count(y2[0])==4:
        columns=True
    else:
        count=count+1
    zmarker = 0
    z=[]
    for r in range(4):
        z.append(l[r][zmarker])
        
if rows==True and columns==True:
    print(f'Everything adds up, this took {count} cycles')

    