from random import randint
l = [[0 for c in range(6)]for r in range(6)]
posX=0
posY=0
oneCount=0
while oneCount!=12:
    posX=randint(0,5)
    posY=randint(0,5)
    if l[posX][posY] ==0:
        l[posX][posY] = 1
        oneCount=oneCount+1
for r in l:
    print(r)
print('-'*30)
            
        
    
