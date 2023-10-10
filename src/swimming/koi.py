from datetime import date


class Koi:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True


jeremy = Koi("Jeremy", "Koi", date.today())
print(jeremy)
