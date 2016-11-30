menuInputList = ['I' ,'E']
itemNameList=[]
itemCountList=[]
itemCostList=[]
orderedCostList=[]

menuInput = input("Press I to input an item's details, and E to Exit").upper()
while menuInput not in menuInputList:
    print("Error")
    menuInput = input("Press I to input an item's details, and E to Exit").upper()

while menuInput == "I":
    itemName = input("Please enter the item name")
    while len(itemName) == 0:
        print("Please enter at least a character.")
        itemName = input("Please enter the item name")
    itemNameList.append(itemName)

    itemCount = int(input("Please enter the number of items"))
    while itemCount < 0:
        print("Please enter a positive number.")
        itemCount = int(input("Please enter the number of items"))
    itemCountList.append(itemCount)

    itemCost = float(input("Please enter the item cost."))
    while itemCost < 0 :
        print("Please enter a positive number.")
        itemCost = float(input("Please enter the item cost."))
    itemCostList.append(itemCost)

    orderedCost = itemCount * itemCost
    orderedCostList.append(orderedCost)

    menuInput = input("Press I to input an item's details, and E to Exit").upper()
    while menuInput not in menuInputList:
        print("Error")
        menuInput = input("Press I to input an item's details, and E to Exit").upper()

totalCost = sum(orderedCostList)

if totalCost >100:
    discount = totalCost * 0.1
    shippingCost = totalCost - discount
else:
    shippingCost = totalCost

print("{:<20}{:<6}{}".format("Item Name", "QTY", "Cost") )

for i in range(0, len(itemNameList),1):
    print("{:<20}{:<6}{}".format(itemNameList[i], itemCountList[i], itemCostList[i]))

print("Your discount is: ${:.2f}".format(discount))

print("Your final shipping cost is: ${:.2f}".format(shippingCost))



