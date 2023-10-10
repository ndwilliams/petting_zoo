from datetime import date


class Frog:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True


leaper = Frog("Leaper", "Frog", date.today())
print(leaper)
