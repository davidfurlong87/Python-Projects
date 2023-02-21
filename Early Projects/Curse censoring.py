from random import sample
from random import choice
from string import ascii_lowercase
print(ascii_lowercase)
curse = ['darn', 'dang','freakin', 'heck', 'shoot']
text = input('Please enter some text.')
l = text.split()
m = ['x'*len(i) if i in curse else i for i in l ]
print(l)
print(m)
print(' '.join(m))
#for item in l:
 #   if item in curse:
        
        
  #      for i in ascii_lowercase:
   #         item = item.replace(i, 'x')
#print(l)