from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarFactory:
    valid_types = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def create_car(self, car_type, model, speed_limit):
        try:
            return self.valid_types[car_type](model, speed_limit)
        except KeyError:
            return