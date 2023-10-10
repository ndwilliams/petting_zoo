from datetime import date


class Goat:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True


goatie = Goat("Goatie", "Goat", date.today())
print(goatie)
