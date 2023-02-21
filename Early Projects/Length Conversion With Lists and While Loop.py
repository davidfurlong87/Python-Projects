i=0
values= ['inches', 'yards', 'miles', 'millimeters', 'centimeters', 'meters']
# l=[[i,(i/36),i/63360, i*25.4, i*2.54, i*0.0254],
#    [i*36,i,i*0.000568182,i*914.4,i*91.44,i*0.9144],
#    [i*63360, i/0.000568182,i, i*1609344.01, i*160934, i*1609.34],
#    [i/25.4,i*0.00109361,i*1609344,i,i*0.1,i*0.001],
#    [i*0.393701,i*0.0109361,i*160934.4,i*10,i,i*0.01],
#    [i*39.3701,i*1.09361,i*0.000621371,i*1000,i*100,i]]
cont=True

while cont==True:
    i = eval(input('Please enter a value: '))
    j=eval(input('''Which unit is this?
Please enter:
1 - Inches
2 - Yards
3 - Miles
4 - Milimetres
5 - Centimetres
6 - Metres
'''))
    k=eval(input('''Which unit are you converting to?
Please enter:
1 - Inches
2 - Yards
3 - Miles
4 - Milimetres
5 - Centimetres
6 - Metres
'''))
    l=[[i,(i/36),i/63360, i*25.4, i*2.54, i*0.0254],
   [i*36,i,i*0.000568182,i*914.4,i*91.44,i*0.9144],
   [i*63360, i/0.000568182,i, i*1609344.01, i*160934, i*1609.34],
   [i/25.4,i*0.00109361,i*1609344,i,i*0.1,i*0.001],
   [i*0.393701,i*0.0109361,i*160934.4,i*10,i,i*0.01],
   [i*39.3701,i*1.09361,i*0.000621371,i*1000,i*100,i]]
    print(f'{i} {values[j-1]} is', l[j-1][k-1], values[k-1])
    print('''Do you want to continue?
Enter:
1 for Yes
2 for No''')
    contcont=eval(input())
    if contcont==2:
        break
        #cont=False
