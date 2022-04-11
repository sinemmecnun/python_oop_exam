from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationFactory:
    valid_types = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    def create_decoration(self, decoration_type):
        return self.valid_types[decoration_type]()
