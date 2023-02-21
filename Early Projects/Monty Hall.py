#to simulate the other door being chose, and for the computer to know what ive chosen, add 1,2,3 together to create6
#subtract from there

#1 equals change, 2 equals no change

#randomdoorhelp has been removed from guesses that were incorrect, the reason being that if its incorrect,
#the only other door offered would be the only remaining door, hence making the line redundant

#looks like in the 3 ==3, 2==2 statements, the random door help is also redundant. remove after debugging
#also, further refine by changing 3==3, 2==2, 1==1 to location==guess(the loop is the same for them all)

#can also refine other state ments to "if location = guess+/-1:"


from random import randint
changeWin=0
changeLose=0
dontChangeWin=0
dontChangeLose=0
for i in range(10000):
    location=randint(1,3)
    guess=randint(1,3)
    
    if location==2 and guess==2:
        inCorrectDoorHelp=randint(1, 2)#1 equals 1, 2 equals 3
        change = randint(1,2)#1 equals change, 2 equals no change
        if inCorrectDoorHelp ==1:
            if change ==1:
                changeLose=changeLose+1
            else:
                dontChangeWin = dontChangeWin+1
        else:
            if change ==1:
                changeLose=changeLose+1
            else:
                dontChangeLose = dontChangeLose+1
    elif location==2 and guess==3:
        change = randint(1,2)#1 equals change, 2 equals no change
        if change ==1 :
            changeWin=changeWin+1
        else:
            changeLose==changeLose+1
    elif location==2 and guess==1:
        change = randint(1,2)#1 equals change, 2 equals no change
        if change ==1 :
            changeWin=changeWin+1
        else:
            dontChangeLose==dontChangeLose+1
            
    elif location==3 and guess==3:
        inCorrectDoorHelp=randint(1, 2)
        change = randint(1,2)#1 equals change, 2 equals no change
        if inCorrectDoorHelp ==1: # i think this whole section can be simplified to if change == 1: (the 2 statements below are the same)
            if change ==1:
                changeLose=changeLose+1
            else:
                dontChangeWin = dontChangeWin+1
        else:
            if change ==1:
                changeLose=changeLose+1
            else:
                dontChangeWin = dontChangeWin+1
    elif location==3 and guess==2:
        change = randint(1,2)#1 equals change, 2 equals no change
        if change ==1 :
            changeWin=changeWin+1
        else:
            dontChangeLose==dontChangeLose+1
    elif location==3 and guess==1:
        change = randint(1,2)#1 equals change, 2 equals no change
        if change ==1 :
            changeWin=changeWin+1
        else:
            dontChangeLose==dontChangeLose+1
        
    elif location==1 and guess==1:
        inCorrectDoorHelp=randint(1, 2)
        change = randint(1,2)#1 equals change, 2 equals no change
        if inCorrectDoorHelp ==1: # i think this whole section can be simplified to if change == 1: (the 2 statements below are the same)
            if change ==1:
                changeLose=changeLose+1
            else:
                dontChangeWin = dontChangeWin+1
        else:
            if change ==1:
                changeLose=changeLose+1
            else:
                dontChangeWin = dontChangeWin+1
    elif location==1 and guess==3:
        change = randint(1,2)#1 equals change, 2 equals no change
        if change ==1 :
            changeWin=changeWin+1
        else:
            dontChangeLose==dontChangeLose+1
    else:# location==1 and guess==2:
        change = randint(1,2)#1 equals change, 2 equals no change
        if change ==1 :
            changeWin=changeWin+1
        else:
            dontChangeLose==dontChangeLose+1
            
print(changeWin)
print(changeLose)
print(dontChangeWin)
print(dontChangeLose)
    

        
   
    