from project.core.car_factory import CarFactory
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []
        self.car_factory = CarFactory()

    def create_car(self, car_type, model, speed_limit):
        model_exists = self.find_car_by_model(model)
        if model_exists:
            raise Exception(f"Car {model} is already created!")

        car = self.car_factory.create_car(car_type, model, speed_limit)

        if car:
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        driver_exists = self.find_driver_by_name(driver_name)
        if driver_exists:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        race_exists = self.find_race_by_name(race_name)
        if race_exists:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        current_driver = self.find_driver_by_name(driver_name)
        if not current_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        new_car = self.filer_cars_for_race(car_type)
        if not new_car:
            raise Exception(f"Car {car_type} could not be found!")

        if current_driver.car is not None:
            old_car = current_driver.car
            current_driver.car = new_car
            old_car.is_taken = False
            new_car.is_taken = True
            return f"Driver {current_driver.name} changed his car from {old_car.model} to {new_car.model}."

        current_driver.car = new_car
        new_car.is_taken = True
        return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        current_driver = self.find_driver_by_name(driver_name)
        current_race = self.find_race_by_name(race_name)
        if not current_race:
            raise Exception(f"Race {race_name} could not be found!")

        if not current_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if current_driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if current_driver in current_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        current_race = self.find_race_by_name(race_name)
        if not current_race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        race_drivers = current_race.drivers
        race_results = sorted(race_drivers, key=lambda x: -x.car.speed_limit)
        race_results = race_results[:3]
        result = ""
        for driver in race_results:
            driver.number_of_wins += 1
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"
        return result.strip()

    def find_car_by_model(self, model):
        for car in self.cars:
            if car.model == model:
                return car
        return None

    def find_driver_by_name(self, driver_name):
        driver = [d for d in self.drivers if d.name == driver_name]
        if not driver:
            return
        return driver[0]

    def find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        return

    def filer_cars_for_race(self, car_type):
        first_filter = [c for c in self.cars if c.__class__.__name__ == car_type]
        final = [c for c in first_filter if not c.is_taken]
        if final:
            return final[-1]
        return
