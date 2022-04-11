from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_UNITS = 15

    def __init__(self, name):
        super().__init__(name, 90)