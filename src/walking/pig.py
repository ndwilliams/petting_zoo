from datetime import date


class Pig:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True


Oink = Pig("Oink", "Pig", date.today())
print(Oink)
