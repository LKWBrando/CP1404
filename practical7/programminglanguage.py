class ProgrammingLanguage:
    def __init__(self, language, status,reflection,year):
        self.language = language
        self.status = status
        self.relection = reflection
        self.year = year

    def is_dynamic(self):
        if self.status == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} typing, Reflection = {}, First appeared in {}". format(self.language, self.status, self.relection, self.year)
