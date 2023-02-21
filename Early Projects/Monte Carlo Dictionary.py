import random
deck = [{'value':i, 'suit':c}
for c in ['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2,15)]
flush_count=0
for J in range(10000):
    random.shuffle(deck)
    l1=[]
    for i in range(5):
        l1.append((deck[i]['value'],deck[i]['suit']))
    l1.sort()
    if l1[0][1]==l1[1][1]==l1[2][1]==l1[3][1]==l1[4][1]:
        print('Player 1 Flush!')
        flush_count+=1
print(f'There were {flush_count} flushes out of 10,000 iterations')
