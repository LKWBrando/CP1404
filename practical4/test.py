dayList = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat',]

def get_day():
    inputDay = int(input("Enter 0 - 6"))
    while inputDay < 0 or inputDay >6:
        print("Error")
        inputDay = int(input("Enter 0 - 6"))
    print("The day of the week is:", dayList[inputDay])

get_day()