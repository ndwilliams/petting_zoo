from datetime import date


class Anaconda:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True


susan = Anaconda("Susan", "Anaconda", date.today())
print(susan)
