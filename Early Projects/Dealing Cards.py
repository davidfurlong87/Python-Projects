import random
deck = [{'value':i, 'suit':c}
for c in ['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2,15)]
random.shuffle(deck)
print(deck)
l1=[]
l2=[]
for i in range(0,6,+2):
    l1.append((deck[i]['value'],deck[i]['suit']))
l1.sort()
print(l1)
for i in range(1,6,+2):
    l2.append((deck[i]['value'],deck[i]['suit']))
l2.sort()
print(l2)
if l1[2][0]>l2[2][0]:
    print('Player 1 wins')
elif l2[2][0]>l1[2][0]:
    print('Player 2 wins')
else:
    print('Round 1 tie!')
    if l1[1][0]>l2[1][0]:
        print('Player 1 wins')
    elif l2[1][0]>l1[1][0]:
        print('Player 2 wins')
    else:
        print('Round 2 Tie')
        if l1[0][0]>l2[0][0]:
            print('Player 1 wins')
        elif l2[0][0]>l1[0][0]:
            print('Player 2 wins')
        else:
            print('Round 3 Tie!')
if l1[0][0]==l1[1][0]==l1[2][0]:
    print('Player 1 3-of-a-kind!')
else:
    l1_count=[l1[i][0] for i in range(3)]
    for i in l1_count:
        if l1_count.count(i)==2:
            print('Player 1 pair!')
            break
if l2[0][0]==l2[1][0]==l2[2][0]:
    print('Player 2 3-of-a-kind!')
else:
    l2_count=[l2[i][0] for i in range(3)]
    for i in l2_count:
        if l2_count.count(i)==2:
            print('Player 2 pair!')
            break
if l1[0][1]==l1[1][1]==l1[2][1]:
    print('Player 1 Flush!')
if l2[0][1]==l2[1][1]==l2[2][1]:
    print('Player 2 Flush!')
if (l1[0][0]+1)==(l1[1][0]) and (l1[1][0]+1)==(l1[2][0]):
    print('Player 1 straight!')
if (l2[0][0]+1)==(l2[1][0]) and (l2[1][0]+1)==(l2[2][0]):
    print('Player 1 straight!')
    