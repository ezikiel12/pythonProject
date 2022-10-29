
def checkRemainder():
    print('Values divisible by 12:')
    counter = 1
    listCounter = 0
    divList = []
    while (counter <= 2000):
        if counter % 12 == 0:
            divList.insert(listCounter, counter)
            listCounter = listCounter + 1
            counter = counter + 1
        else: counter = counter + 1
    print(divList)

def checkMult():
    print('Multiples of 5:')
    counter = 1
    listCounter = 0
    multList = []
    while (counter <= 2000):
        if counter % 5 == 0:
            multList.insert(listCounter, counter)
            listCounter = listCounter + 1
            counter = counter + 1
        else: counter = counter + 1
    print(multList)

checkRemainder()
checkMult()
