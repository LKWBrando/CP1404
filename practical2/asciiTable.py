lower = 10
upper = 100
print("Enter a number ({}-{})".format(lower, upper))

print("{:<10}{:<15}".format("Name", "ASCII value"))

for i in range(10,120,11):
    print("{:<10}{:<15}".format(i,chr(i)))