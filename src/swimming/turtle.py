from datetime import date


class Turtle:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True


mitch = Turtle("Mitch", "Turtle", date.today())
print(mitch)
