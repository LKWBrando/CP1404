from practical7.guitar import Guitar


guitar_list = []

count = 0
while count == 0:
    input_name = input("Please enter your name.")
    if input_name == "" or input_name.isspace():
        count = 1
    else:
        input_year = int(input("Input year."))
        input_cost = int(input("Input cost"))
        guitar_list.append(Guitar(input_name, input_year, input_cost))


for guitar in guitar_list:
    index = 0
    guitar_age = guitar.get_age()
    if guitar.is_vintage(guitar_age) == True:
        print("Guitar {}: {} ({}), worth ${} ({})".format(index + 1, guitar.name, guitar.year, guitar.cost, "Vintage"))
    else:
        print(
            "Guitar {}: {} ({}), worth ${}".format(index + 1, guitar.name, guitar.year, guitar.cost))