grid=[[0,'M',0,'M',0],
      [0,0,'M',0,0],
      [0,0,0,0,0],
      ['M','M',0,0,0],
      [0,0,0,'M',0]]
count=0
column=0
row=0
for r in grid:
    print(r)
print()
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
            
