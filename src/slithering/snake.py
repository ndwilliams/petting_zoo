from datetime import date


class Snake:
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True


sneaker = Snake("Sneaker", "Snake", date.today())
print(sneaker)
