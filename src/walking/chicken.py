from datetime import date


class Chicken:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True


pecker = Chicken("Pecker", "Chicken", date.today())
print(pecker)
