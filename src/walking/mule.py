from datetime import date


class Mule:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True


loafer = Mule("Loafer", "Mule", date.today())
print(loafer)
