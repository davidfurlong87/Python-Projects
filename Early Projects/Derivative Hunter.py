powerNumber = input('Please enter some power!: ')
powerLocation = powerNumber.index('*')
timesPower = powerNumber[powerLocation+2:]
timesPowerInt = int(timesPower)
convertedInt = timesPowerInt - 1
derivative = timesPower + '*' + powerNumber[powerLocation+1:]
print(timesPower, '*', powerNumber[:powerLocation], '**', convertedInt, sep='')