from datetime import date


class Llama:
    def __init__(self, name, species, date_added):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True


miss_fuzz = Llama("Miss Fuzz", "domestic llama", date.today())
print(miss_fuzz)

attributes = vars(miss_fuzz)
print(attributes)

for key in attributes.keys():
    print(f"{key}: {attributes[key]}")
