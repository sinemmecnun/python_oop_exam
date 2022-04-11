from abc import ABC


class Astronaut(ABC):
    OXYGEN_UNITS = 10

    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.OXYGEN_UNITS
        return

    def increase_oxygen(self, amount):
        self.oxygen += amount
        return
