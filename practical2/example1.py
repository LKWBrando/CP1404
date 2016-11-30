finished = False

result = 0

while not finished:
    try:
        number1 = int(input("Enter a number"))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", result)