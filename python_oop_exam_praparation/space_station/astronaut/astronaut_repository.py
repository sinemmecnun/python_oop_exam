from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut not in self.astronauts:
            return
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        astronaut = [a for a in self.astronauts if a.name == name]
        if astronaut:
            result = astronaut[0]
            return result
