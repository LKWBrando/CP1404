count = {}

inputString = input("Please enter your text.")
stringCount = inputString.split()
stringCount.sort()

print(stringCount)

for word in stringCount:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

maxLength = max(len(word) for word in count)

for each,count[each] in sorted(count.items()):
    print("{:{}}:{}".format(each, maxLength, count[each]))
