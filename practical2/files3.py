dataList = []
numbers_txt = open("numbers.txt", "r")

for num in numbers_txt:
    data = int(num)
    print(data)
    dataList.append(data)
numbers_txt.close()

total = sum(dataList)
print("The total is: ",total)