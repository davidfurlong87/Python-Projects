fraction=input(('Please enter a fraction in the format x/x: '))
l = fraction.split('/')
m=[]
for i in range(int(max(l)),0,-1):
    if int(l[0])%i==0 and int(l[1])%i==0:
        x =(int(l[0])/i)
        y= (int(l[1])/i)
        m.append(int(x))
        m.append(int(y))
        break
#         m.append(int(l[0]))/i
#         m.append(int(l[1]))/i
print('The lowest term this fraction can be represented in are: {:d} / {:d}'.format(m[0], m[1]))
        