lists=[]
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                lists.append(int(i+j))
                lists.append(int(i+k))
                lists.append(int(i+l))
                lists.append(int(j+k))
                lists.append(int(j+l))
                lists.append(int(k+l))
for i in range(2,13):
    print('The value of', i, 'occurred', lists.count(i), 'times')