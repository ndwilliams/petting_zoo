from datetime import date


class Duck:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True


quacker = Duck("Quacker", "Duck", date.today())
print(quacker)
