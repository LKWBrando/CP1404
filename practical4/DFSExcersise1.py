import random

overallList = []

userInput = int(input("How many quick picks do you want to generate?"))

for input in range (0,userInput,1):
    numberList = []
    for i in range (0,6,1):
        randNumber = random.randint(1,45)
        while randNumber in numberList:
            randNumber = random.randint(1,45)
        numberList.append(randNumber)
        numberList.sort()
    overallList.append(numberList)

for list in overallList:
    for num in list:
        print("{:<2}".format(num), end=" ")
    print()