from project.baked_food.bread import Bread
from project.baked_food.cake import Cake


class FoodFactory:
    valid_types = {
        "Bread": Bread,
        "Cake": Cake
    }

    def create_food(self, food_type, name, price):
        return self.__class__.valid_types[food_type](name, price)