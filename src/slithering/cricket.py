from datetime import date


class Cricket:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True


chirper = Cricket("Chirper", "Cricket", date.today())
print(chirper)
