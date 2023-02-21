age = eval(input('Whats your age?: '))
gender = eval(input('Whats your gender? (Enter 1 for  Male and 2 for Female)'))
units=int(input('Which units would you prefer to use, Metric or Imperial? (Enter 1 for  Metric and 2 for Imperial)'))
height = 0
weight = 0
bmr = 0
if units==1:
    height = eval(input('Whats your height in CM?'))
    weight = eval(input('Whats your weight in KG?'))
    if gender == 1:
        bmr=88.362+(13.397*weight)+(4.799*height)-(5.677*age)
    else:
        bmr=447.593+(9.247*weight)+(3.098*height)-(4.330*age)
    print('Your BMR is', bmr)