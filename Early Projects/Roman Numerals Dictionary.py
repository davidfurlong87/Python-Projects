numerals={'m':1000, 'd':500, 'c':100, 'l':50, 'x':10, 'v':5, 'i':1}
example=input('Enter some Roman numerals: ')
conversion=0
for i in range(len(example)):
    if example[i].lower()=='v' and example[i-1] =='i':
        conversion+=3
    elif example[i].lower()=='x' and example[i-1] =='i':
        conversion+=8
    elif example[i].lower()=='l' and example[i-1] =='x':
        conversion+=30
    else:
        conversion+=numerals[example[i]]
print(conversion)

        
    