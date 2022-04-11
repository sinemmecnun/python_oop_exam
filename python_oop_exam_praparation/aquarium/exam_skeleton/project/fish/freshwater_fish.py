from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    SIZE_INCREMENT = 3
    AQUARIUM_TYPE = "FreshwaterAquarium"

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)
