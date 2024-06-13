class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None) -> None:
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception('This is not an acceptable pet')
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

class Owner:
    
    def __init__(self, name) -> None:
        self.name = name

    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception('This is not an acceptable animal')
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        return sorted_pets

# Pet('Luca', 'dog')
# Pet('Andrea', 'dog')
# Owner('Jazz').get_sorted_pets()

# breakpoint()