from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class FishFactory:
    valid_types = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    def create_fish(self, fish_type, fish_name, fish_species, price):
        return self.valid_types[fish_type](fish_name, fish_species, price)
