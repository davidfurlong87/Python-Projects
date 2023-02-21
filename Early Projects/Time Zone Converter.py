time = input('Please enter a string for your current time:')
firstColon=time.index(':')
print('first colon is', firstColon) #tracker
hours=int(time[:firstColon])
print('the hours are', hours) #tracker
print('''What time zone are you currently in?
Choose:
(1) Eastern
(2) Central
(3) Mountain
(4) Pacific''')
timeZone = eval(input())
convertedHours = ''
convertedTime = ''
if timeZone == 1:
    print('''You are currently in the Eastern Time Zone, which time zone would you like to show?
    Choose:
    (1) Eastern
    (2) Central
    (3) Mountain
    (4) Pacific''')
    desiredTimeZone = eval(input())
    if desiredTimeZone == 1:
        convertedTime = time
        print('The current time in the Eastern zone is:', convertedTime)
    elif desiredTimeZone == 2:
        convertedHours = (hours-1)
        
        print('The current time in the Central zone is:', convertedTime)
    elif desiredTimeZone == 3:
        convertedHours = hours-1
        
        print('The current time in the Central zone is:', convertedTime)
        #-1

convertedTime = str(convertedHours) + time[firstColon:]
print(convertedTime)


#if time - x <1 or time + x > 12:
    #am changes to pm
    