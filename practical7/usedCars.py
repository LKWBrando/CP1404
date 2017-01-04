"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from practical7.cars import Car

def main():
    bus = Car(180)
    bus.drive(30)
    limo = Car("limo",100)

    limo.add_fuel(20)
    print("fuel for limo =", limo.fuel)
    limo.drive(115)
    print("odometer for limo=", limo.odometer)
    print(limo)

"""
    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=bus))
"""

main()