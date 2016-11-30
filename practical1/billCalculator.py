priceRate = float(input("Please enter the price per kWh."))
usageRate = float(input("Please enter the daily amount used."))
daysBilled = int(input("Please enter the number of billing days."))

finalBill = priceRate + usageRate + daysBilled


tarrif11 = 0.244618
tarrif31 = 0.136928

tarrifList = ['11', '31']
tarrifChosen = input("Please enter 11 for tarrif11 and 31 for tarrif31.")
while tarrifChosen not in tarrifList:
    print("Error")
    tarrifChosen = input("Please enter 11 for tarrif11 and 31 for tarrif31.")

    if tarrifChosen == "11":
        tarrifChosen = tarrif11
    else:
        tarrifChosen = tarrif31

usageRate = float(input("Please enter the daily amount used."))
daysBilled = int(input("Please enter the number of billing days."))
finalBill = priceRate + usageRate + daysBilled