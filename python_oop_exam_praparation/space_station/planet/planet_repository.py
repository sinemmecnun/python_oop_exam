from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet not in self.planets:
            return
        self.planets.remove(planet)

    def find_by_name(self, name):
        planet = [p for p in self.planets if p.name == name]
        if planet:
            result = planet[0]
            return result