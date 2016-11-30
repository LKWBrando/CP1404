"""
lower = 10
upper = 100
print("Enter a number ({}-{})".format(lower, upper))

print("{:<10}{:<15}".format("Name", "ASCII value"))

for i in range(10,120,11):
    print("{:<10}{:<15}".format(i,chr(i)))
"""
lower = 10
upper = 100

def get_number(lower,upper):
    finished = False
    while not finished:
        try:
            userInput = int(input("Please enter a number between 10-100 "))
            while userInput < lower or userInput > upper:
                print("Number not in range!")
                userInput = int(input("Please enter a number between 10-100"))
            print("{:<10}{:<15}".format("Name", "ASCII value"))
            print("{:<10}{:<15}".format(userInput, chr(userInput)))
            finished = True
        except ValueError:
            print("Input must be an integer!")

get_number(lower,upper)