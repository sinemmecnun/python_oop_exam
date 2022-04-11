from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_UNITS = 5

    def __init__(self, name):
        super().__init__(name, 70)