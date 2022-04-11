from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("Test", 10)

    def test_object_initialized_correctly(self):
        name = "Test"
        capacity = 10

        train = Train(name, capacity)

        self.assertEqual(name, train.name)
        self.assertEqual(capacity, train.capacity)
        self.assertEqual([], train.passengers)

    def test_train_class_attributes(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add_to_full_train_raises(self):
        self.train.capacity = 0
        with self.assertRaises(ValueError) as ex:
            self.train.add("Test")
        self.assertEqual("Train is full", str(ex.exception))
        self.assertEqual([], self.train.passengers)

    def test_add_existing_passenger_raises(self):
        passenger_name = "Test"
        self.train.passengers = [passenger_name]
        with self.assertRaises(ValueError) as ex:
            self.train.add(passenger_name)
        self.assertEqual(f"Passenger {passenger_name} Exists", str(ex.exception))
        self.assertEqual([passenger_name], self.train.passengers)

    def test_add_passenger_successfully(self):
        passenger_name = "Test"
        result = self.train.add(passenger_name)
        self.assertEqual(f"Added passenger {passenger_name}", result)
        self.assertEqual([passenger_name], self.train.passengers)

    def test_remove_non_existent_passenger(self):
        passenger_name = "Test"
        expected_result = "Passenger Not Found"
        with self.assertRaises(ValueError) as ex:
            self.train.remove(passenger_name)
        self.assertEqual(expected_result, str(ex.exception))

    def test_remove_passenger_successfully(self):
        passenger_name = "Test"
        self.train.passengers = [passenger_name]
        result = self.train.remove(passenger_name)
        self.assertEqual(f"Removed {passenger_name}", result)
        self.assertEqual([], self.train.passengers)


if __name__ == '__main__':
    main()
