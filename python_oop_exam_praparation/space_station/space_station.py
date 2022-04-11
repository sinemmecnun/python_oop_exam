from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type, name):
        valid_types = ["Biologist", "Geodesist", "Meteorologist"]
        if astronaut_type not in valid_types:
            raise Exception("Astronaut type is not valid!")

        astronaut = self.find_astronaut(name)
        if astronaut:
            return f"{name} is already added."

    def add_planet(self, name, items):
        pass

    def retire_astronaut(self, name):
        pass

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut += 10
        return

    def send_on_mission(self, planet_name):
        pass

    def report(self):
        pass

    def find_astronaut(self, name_temp):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name_temp:
                return astronaut
