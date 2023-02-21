import math
number=eval(input('Please enter a positive number to determine its square root'))
if number<0:
    print('Sorry, please enter a positive number.')
else:
    print(math.sqrt(number))