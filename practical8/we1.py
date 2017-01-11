"""
CP1404/CP5632 Practical
Car class
"""
import random

class Car:
    """ represent a car object """
    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0
        self.price_per_km = 1.20

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven

class Taxi(Car):
    """ specialised version of a Car that includes fare costs """
    def __init__(self, name, fuel, price_per_km):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        Taxi.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance, self.price_per_km)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

class UnreliableCar(Car):

    def __init__(self,name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        rand_num = random.randint(0,100)
        if rand_num < self.reliability:
            if distance > self.fuel:
                distance_driven = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
                distance_driven = distance
            self.odometer += distance_driven
            return distance_driven
        else:
            print("Do not drive car")

class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness, price_per_km =1.2):
        super().__init__(name, fuel, price_per_km)
        self.price_per_km = fanciness * 1.2
        self.flagfall = 4.5
        self.current_fare_distance = 0

    def get_fare(self):
        return (self.price_per_km * self.current_fare_distance) + self.flagfall

"""
prius1 = Taxi("Prius1", 100, 1.2)
prius1.drive(40)
print(prius1)
print("Cost of current fare is: ${}".format(prius1.get_fare()))

prius1.start_fare()
prius1.drive(100)
print(prius1)
print("Cost of current fare is: ${}".format(prius1.get_fare()))

prius2 = UnreliableCar("Prius2", 100, 10)
prius2.drive(50)
print(prius2)

prius3 = SilverServiceTaxi("Prius3", 100, 2)
print(prius3)
prius3.drive(10)
print(prius3.get_fare())
"""