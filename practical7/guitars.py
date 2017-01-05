from practical7.guitar import Guitar
nameList = []
yearList = []
costList = []

checker = 1
while True:
        name = input("Name:")
        if name != "":
            nameList.append(name)
            year = input("Year:")
            yearList.append(year)
            cost = input("Cost:$")
            costList.append(cost)
        else:
            break

for i in range(len(nameList)):
    print(Guitar(nameList[i], yearList[i], costList[i]))