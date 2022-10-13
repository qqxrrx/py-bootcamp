class Pet:
    # class attribute, shared across all instances
    # however if you change this value to an instance, it will be exclusive to that instance only
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"can't have a {species} pet")

        # instance attributes
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"can't have a {species} pet")
        self.species = species


cat = Pet("C1", "cat")
dog = Pet("D1", "dog")
croc = Pet("CR", "croc")
