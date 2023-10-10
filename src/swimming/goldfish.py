from datetime import date


class Goldfish:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True


goldie = Goldfish("goldie", "Goldfish", date.today())
print(goldie)
