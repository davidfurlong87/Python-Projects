x = 0
for i in range (5):
    print('Please enter a number between 1 and 5')
    number=eval(input())
    if number%2==0:
        x = x+number
print('The sum of all even numbers you entered is:', x)