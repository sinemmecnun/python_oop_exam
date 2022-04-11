from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Test")

    def test_object_initialized_correctly(self):
        pet_shop = PetShop("Test")
        self.assertEqual("Test", pet_shop.name)
        self.assertEqual({}, pet_shop.food)
        self.assertEqual([], pet_shop.pets)

    def test_repr_override_works_correctly_no_pets(self):
        expected_result = f'Shop {self.pet_shop.name}:\n' \
                        f'Pets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(expected_result, repr(self.pet_shop))

    def test_repr_override_works_correctly_with_pets(self):
        self.pet_shop.pets = ["Dof", "Bailey"]
        expected_result = f'Shop {self.pet_shop.name}:\n' \
                          f'Pets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(expected_result, repr(self.pet_shop))

    def test_add_food_with_zero_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("kibble", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_with_negative_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("kibble", -10)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_increase_quantity_existing_food(self):
        self.pet_shop.food = {"Kibble": 10}
        result = self.pet_shop.add_food("Kibble", 10)
        expected_result = f"Successfully added 10.00 grams of Kibble."
        self.assertEqual(expected_result, result)
        self.assertEqual({"Kibble": 20}, self.pet_shop.food)

    def test_add_new_food(self):
        result = self.pet_shop.add_food("kibble", 10)
        expected_result = f"Successfully added 10.00 grams of kibble."
        self.assertEqual(expected_result, result)
        self.assertEqual({"kibble": 10}, self.pet_shop.food)

    def test_try_add_existing_pet_raises(self):
        name = "Test"
        self.pet_shop.pets.append(name)
        self.assertEqual([name], self.pet_shop.pets)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet(name)
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual([name], self.pet_shop.pets)

    def test_add_new_pet_to_list(self):
        name = "Test"
        self.assertEqual([], self.pet_shop.pets)
        result = self.pet_shop.add_pet(name)
        self.assertEqual(f"Successfully added {name}.", result)
        self.assertEqual([name], self.pet_shop.pets)

    def test_feed_non_existent_pet_raises(self):
        pet_name = "Test"
        food_name = "Kibble"

        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_non_existent_food(self):
        pet_name = "Test"
        food_name = "Kibble"
        self.pet_shop.pets.append(pet_name)
        self.assertEqual([pet_name], self.pet_shop.pets)
        self.assertEqual({}, self.pet_shop.food)
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(f'You do not have {food_name}', result)

    def test_feed_pets_with_not_enough_food(self):
        self.pet_shop.food = {"Kibble": 10}
        pet_name = "Test"
        food_name = "Kibble"
        self.pet_shop.pets.append(pet_name)
        self.assertEqual([pet_name], self.pet_shop.pets)
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual("Adding food...", result)
        self.assertEqual({"Kibble": 1010}, self.pet_shop.food)

    def test_successfully_feed_pet(self):
        self.pet_shop.food = {"Kibble": 100}
        pet_name = "Test"
        food_name = "Kibble"
        self.pet_shop.pets.append(pet_name)
        self.assertEqual([pet_name], self.pet_shop.pets)
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(f"{pet_name} was successfully fed", result)
        self.assertEqual({"Kibble": 0}, self.pet_shop.food)


if __name__ == '__main__':
    main()