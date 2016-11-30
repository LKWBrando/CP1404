"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
__author__ = 'Lindsay Ward'
"""

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()


def getCelsius():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def getFahrenheit():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))


while choice != "Q":
    if choice == "C":
        getCelsius()
    elif choice == "F":
        getFahrenheit()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

