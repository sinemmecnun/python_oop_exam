from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("Test", 12)

    def test_factory_initialized_correctly(self):
        name = "Test"
        capacity = 12
        paint_factory = PaintFactory(name, capacity)
        valid_ingredients = ["white", "yellow", "blue", "green", "red"]

        self.assertEqual(name, paint_factory.name)
        self.assertEqual(capacity, paint_factory.capacity)
        self.assertEqual(valid_ingredients, paint_factory.valid_ingredients)
        self.assertEqual({}, paint_factory.ingredients)

    def test_products_property_method_returns(self):
        self.assertEqual({}, self.paint_factory.products)

    def test_can_add_methods_returns_false(self):
        self.assertEqual(True, self.paint_factory.can_add(12))

    def test_can_add_methods_returns_true(self):
        self.assertEqual(False, self.paint_factory.can_add(123))

    def test_can_add_with_capacity_left(self):
        self.paint_factory.ingredients = {"white": 11}
        self.assertEqual(True, self.paint_factory.can_add(1))

    def test_can_add_with_no_capacity_left(self):
        self.paint_factory.ingredients = {"white": 11, "yellow": 1}
        self.assertEqual(False, self.paint_factory.can_add(1))

    def test_repr_with_no_ingredients(self):
        expected_result = f"Factory name: {self.paint_factory.name} with capacity {self.paint_factory.capacity}.\n"
        self.assertEqual(expected_result, repr(self.paint_factory))

    def test_repr_with_ingredients(self):
        self.paint_factory.ingredients = {"white": 11, "yellow": 1}
        expected_result = f"Factory name: {self.paint_factory.name} with capacity {self.paint_factory.capacity}.\n"
        # for ingredient in self.paint_factory.ingredients:
        #     expected_result += f"{ingredient}: {self.paint_factory.ingredients[ingredient]}\n"
        expected_result += "white: 11\nyellow: 1\n"
        self.assertEqual(expected_result, repr(self.paint_factory))

    def test_add_non_valid_ingredient_raises(self):
        product_type = "pink"
        product_quantity = 13
        expected_result = f"Ingredient of type {product_type} not allowed in {self.paint_factory.__class__.__name__}"
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient(product_type, product_quantity)
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_add_no_capacity_left_raises(self):
        product_type = "blue"
        product_quantity = 13
        expected_result = "Not enough space in factory"
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient(product_type, product_quantity)
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_add_new_ingredient(self):
        product_type = "blue"
        product_quantity = 1
        self.paint_factory.add_ingredient(product_type, product_quantity)
        self.assertEqual({product_type: product_quantity}, self.paint_factory.ingredients)

    def test_add_increase_quantity_of_existing_ingredient(self):
        product_type = "blue"
        product_quantity = 1
        self.paint_factory.ingredients = {product_type: 2}
        self.paint_factory.add_ingredient(product_type, product_quantity)
        self.assertEqual({product_type: 3}, self.paint_factory.ingredients)

    def test_remove_non_existent_ingredient_raises(self):
        product_type = "blue"
        product_quantity = 1
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient(product_type, product_quantity)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_remove_ingredient_with_negative_quantity(self):
        product_type = "blue"
        product_quantity = 3
        self.paint_factory.ingredients = {product_type: 2}
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient(product_type, product_quantity)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))
        self.assertEqual({product_type: 2}, self.paint_factory.ingredients)

    def test_remove_ingredient_successfully(self):
        product_type = "blue"
        product_quantity = 2
        self.paint_factory.ingredients = {product_type: 2}
        self.paint_factory.remove_ingredient(product_type, product_quantity)
        self.assertEqual({product_type: 0}, self.paint_factory.ingredients)


if __name__ == '__main__':
    main()