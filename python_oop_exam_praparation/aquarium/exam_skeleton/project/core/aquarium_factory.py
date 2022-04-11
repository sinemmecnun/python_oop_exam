from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium


class AquariumFactory:
    valid_types = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    def create_aquarium(self, aquarium_type, aquarium_name):
        return self.valid_types[aquarium_type](aquarium_name)
