from project.core.aquarium_factory import AquariumFactory
from project.core.decoration_factory import DecorationFactory
from project.core.fish_factory import FishFactory
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []
        self.aquarium_factory = AquariumFactory()
        self.decoration_factory = DecorationFactory()
        self.fish_factory = FishFactory()

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self.aquarium_factory.valid_types.keys():
            return "Invalid aquarium type."

        aquarium = self.aquarium_factory.create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self.decoration_factory.valid_types.keys():
            return "Invalid decoration type."

        decoration = self.decoration_factory.create_decoration(decoration_type)
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.find_decoration_by_type(decoration_type)
        aquarium = self.find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return
        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}."
        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in self.fish_factory.valid_types.keys():
            return f"There isn't a fish of type {fish_type}."

        fish = self.fish_factory.create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.find_aquarium_by_name(aquarium_name)
        result = aquarium.add_fish(fish)
        return result

    def feed_fish(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        return sum(f.price for f in aquarium.fish) + sum(d.price for d in aquarium.decorations)

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"
        return result.strip()

    def find_decoration_by_type(self, decoration_type):
        decoration = [d for d in self.decorations_repository.decorations if d.__class__.__name__ == decoration_type]
        if not decoration:
            return
        return decoration[0]

    def find_aquarium_by_name(self, aquarium_name):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if not aquarium:
            return
        return aquarium[0]