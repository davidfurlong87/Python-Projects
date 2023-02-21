height = int(input('How high would you like the diamond to be?'))
line=int((height-1)/2)
for i in range(line):
    print(' '*line, 'x', 'x '*i)
    line=line-1
print('x '*(height-2))
line=int((height-1)/2)
for i in range(line, 0, -1):
    print(' '*line-2, 'x', 'x '*i)
    line=line+1