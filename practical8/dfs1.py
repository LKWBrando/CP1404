from practical8.we1 import Taxi
from practical8.we1 import SilverServiceTaxi

menu_input_list = ['c', 'd', 'q']

limo = Taxi("Limo", 100, 1.2)
prius = Taxi("Prius", 100, 1.2)
hummer = Taxi("Hummer", 200, 1.2)
car_list = [limo, prius, hummer]

select_input = 5

def menu():
    menu_input = str(input("q)uit, c)hoose taxi, d)rive")).lower()
    while menu_input not in menu_input_list:
        print ("Invalid Option.")
        menu_input = str(input("q)uit, c)hoose taxi, d)rive")).lower()
    return menu_input

print("Lets Drive!")
menu_input = menu()

menu_count = 1

while menu_count == 1:

    if menu_input == 'c' :
        print("Taxis available")
        for i in range(0, len(car_list)):
            print("{} - {}".format(i, car_list[i]))
        select_input = int(input("Choose Taxi:"))
        print("Bill to date :${}".format(limo.get_fare() + prius.get_fare() + hummer.get_fare()))
        menu_input = menu()

    elif menu_input == 'd':
        dist_input = int(input("Drive how far?"))
        drive_dist = car_list[select_input].drive(dist_input)
        trip_fare = drive_dist * car_list[select_input].price_per_km
        print("That trip cost you ${}".format(trip_fare))
        print("Bill to date :${}".format(limo.get_fare() + prius.get_fare() + hummer.get_fare()))
        menu_input = menu()

    else:
        print("Bill to date :${}".format(limo.get_fare() + prius.get_fare() + hummer.get_fare()))
        print("Taxis are now:")
        for i in range(0, len(car_list)):
            print("{} - {}".format(i, car_list[i]))
        menu_count = 0