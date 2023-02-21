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
print('Budget Shopping Time!')
print()
search_term=eval(input('please enter the maximum youd liek to spend: $'))
for d in products:
    if int(products[d])<=search_term:
        print(d, '${:s}'.format(products[d]))

    

