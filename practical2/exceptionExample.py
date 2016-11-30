try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#1. ValueError occurs when the input numerator and denominator is not an integer

#2. ZeroDivisionError occurs when the denominator is 0

#3. Yes, an error checking loop can be used to print error messages should the input for the denominator equals 0