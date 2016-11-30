def main():
    userName = get_name()
    get_letters(userName)


def get_letters(userName):
    for i in range(1, len(userName), 2):
        print(userName[i])


def get_name():
    userName = str(input("Enter your name."))
    while len(userName) < 1:
        print("No blank entries are allowed")
        userName = str(input("Enter your name."))
    return userName


main()
