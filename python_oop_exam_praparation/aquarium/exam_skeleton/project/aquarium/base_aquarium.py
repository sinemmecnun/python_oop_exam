from abc import ABC

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        comfort = [c.comfort for c in self.decorations]
        return sum(comfort)

    def add_fish(self, fish: BaseFish):
        if len(self.fish) == self.capacity:
            return f"Not enough capacity."

        current_aquarium = self.__class__.__name__
        if fish.AQUARIUM_TYPE != current_aquarium:
            return "Water not suitable."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        if fish not in self.fish:
            return
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\nFish: "
        if not self.fish:
            result += "none\n"
        else:
            result += " ".join([f.name for f in self.fish]) + "\n"
        result += f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
        return result
