from project.drink.tea import Tea
from project.drink.water import Water


class DrinkFactory:
    valid_types = {
        "Tea": Tea,
        "Water": Water
    }

    def create_drink(self, drink_type, name, portion, brand):
        return self.valid_types[drink_type](name, portion, brand)