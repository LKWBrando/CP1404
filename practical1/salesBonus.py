"""
Intermediate Excercise
Practical 1
"""

sales= float(input("Please enter your sales amount."))
while sales >0:
    if sales <1000:
        bonus =  sales * 0.1
    else:
        bonus = sales * 0.15
    print("Your bonus is: $" + str(bonus))
    sales = float(input("Please enter your sales amount."))