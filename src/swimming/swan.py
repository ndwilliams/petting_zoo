from datetime import date


class Swan:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True


lake = Swan("Lake", "Swan", date.today())
print(lake)
