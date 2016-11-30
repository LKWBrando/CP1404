#Practice example for Week 3 lecture


try:
    inputFile = input("Please enter the name")
    fileName = open("inputFile", "r")
    fileName.read()
    fileName.close()
except IOError:
    print("Please enter again.")



