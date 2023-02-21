products={}
stop=False
while stop==False:
    k=input(('Please enter a product name: '))
    if k in products:
        print('Product already found')
        continue
    v=eval(input('Please enter a price: $'))
    products[k.lower()]=str(v)
    prompt=''
    while prompt!='no' or prompt!='yes':
        prompt=input('Do you wish to continue (yes/no)')
        if prompt=='no':
            stop=True
            break
        elif prompt=='yes':
            break
        else:
            prompt==''
for d in products: 
        print('{:^10s}'.format(d), '${:^s}'.format(products[d]))
print()
print('Product search time!')
prompt=''
stop=False
while stop==False:
    item=input('Please enter an item to search for: ')
    if item.lower() in products:
        print('${:s}'.format(products[item]))
    else:
        print('Not found')
    prompt=''
    while prompt!='no' or prompt!='yes':
        prompt=input('Do you wish to continue (yes/no)')
        if prompt=='no':
            stop=True
            break
        elif prompt=='yes':
            break
        else:
            prompt==''

    
