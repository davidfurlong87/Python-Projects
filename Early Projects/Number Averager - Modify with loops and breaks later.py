#This code can be modified with loops and breaks.
#Could repeatedly ask for more numbers until the user says no.
#After the code breaks in this way, I must make a system for collating all the numbers, perhaps by creating and appending a list.
#If I limit myself to the below variables, this will not be possible.

num1 = eval(input('Enter a number: '))
num2 = eval(input('Enter a number: '))
num3 = eval(input('Enter a number: '))
total = num1 + num2 + num3
average = (total)/3 
print('The total is', total)
print('The average is', average)