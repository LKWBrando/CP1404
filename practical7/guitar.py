class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}), worth ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        current_year = 2016
        guitar_age = current_year - self.year
        return guitar_age

    def is_vintage(self, guitar_age):
        if guitar_age >= 50:
            return True
        else:
            return False
