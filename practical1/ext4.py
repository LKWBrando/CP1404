x = int(input("Input the first number, x"))
y = int(input("Input the second number, y"))
if x > y:
    print("Please allow for y to be larger than x")
    x = int(input("Input the first number, x"))
    y = int(input("Input the second number, y"))

print("Even numbers between the numbers provided are:")
for i in range(x,y,1):
    while i%2 == 0:
        print(i, end=' ')
        i = i + 1
print()
print("Odd numbers between the numbers provided are:")
for i in range(x,y,1):
    while i%2 > 0:
        print(i, end=' ')
        i = i + 1

print()
print("The squared values of the range of numbers provided are:")
for i in range(x,y,1):
    print(i**2, end=' ')

