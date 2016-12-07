numberList = []
count = 5

for i in range(0,5,1):
    numberInput = int(input("Please enter {} more number(s)".format(count)))
    count = count - 1
    numberList.append(numberInput)

for num in numberList:
    print("Number: {}".format(num))


print("The first number is {}".format(numberList[0]))

print("The last number is {}".format(numberList[-1]))

print("The smallest number is {}".format(min(numberList)))

print("The largest number is {}".format(max(numberList)))

print("The average of the numbers is {}".format(sum(numberList)/len(numberList)))