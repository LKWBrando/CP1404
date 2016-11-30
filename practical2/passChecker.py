MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"

def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")

    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")

    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)

def is_valid_password(password):
    # TODO: if length is wrong, return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower = count_lower + 1
        if char.isupper():
            count_upper = count_upper + 1
        if char.isdigit():
            count_digit = count_digit + 1
        if char in SPECIAL_CHARACTERS:
            count_special = count_special + 1

    while SPECIAL_CHARS_REQUIRED == False:
        if count_special > 0:
            return False
        while count_lower > 0 and count_upper > 0 and count_digit > 0:
            totalCount = count_lower + count_upper + count_digit
            if totalCount < 7 and totalCount >1:
                return True
            else:
                return False
        return False

    while count_lower > 0 and count_upper > 0 and count_digit > 0 and count_special > 0:
        totalCount = count_lower + count_upper + count_digit + count_special
        if totalCount < 7 and totalCount > 1:
            return True
        else:
            return False
    return False

main()