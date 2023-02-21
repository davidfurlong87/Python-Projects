
for i in range(1, 10001):
    x = 0
    for j in range(1, i):
        if i%j ==0:
            #print(j, 'is a divisor of', i)
            x = x + j
    if x ==i:
        print(i, 'is a perfect number')
        
   