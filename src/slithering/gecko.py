from datetime import date


class Gecko:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True


slime = Gecko("Slime", "Gecko", date.today())
print(slime)
