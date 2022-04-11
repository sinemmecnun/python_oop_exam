import unittest

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.core.drink_factory import DrinkFactory
from project.core.food_factory import FoodFactory
from project.core.table_factory import TableFactory
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class BakeryTests(unittest.TestCase):
    def test_init_bread(self):
        bread = Bread("Test", 12)
        with self.assertRaises(ValueError) as ex:
            bread = Bread("   ", 12)
        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))
        # self.assertEqual("Test", bread.name)
        # self.assertEqual(200, bread.portion)
        # self.assertEqual(12, bread.price)

    def test_repr_baked_food(self):
        bread = Cake("Test", 12)
        exp_result = f" - Test: 245.00g - 12.00lv"
        self.assertEqual(exp_result, str(bread))

    def test_food_factory_create(self):
        food_type = "Bread"
        name = "nz"
        price = 12
        factory = FoodFactory()
        result = factory.create_food(food_type, name, price)
        bread = Bread(name, price)
        self.assertEqual(bread.name, result.name)

    def test_drink_factory_create(self):
        drink_type = "Tea"
        name = "test"
        portion = 12
        brand = "nz"
        drink_factory = DrinkFactory()
        result = drink_factory.create_drink(drink_type, name, portion, brand)
        tea = Tea(name, portion, brand)
        self.assertEqual(tea.name, result.name)

    def test_table_factory(self):
        table_type = "InsideTable"
        table_number = 12
        capacity = 10
        table_factory = TableFactory()
        result = table_factory.create_table(table_type, table_number, capacity)
        table = InsideTable(table_number, capacity)
        self.assertEqual(table.table_number, result.table_number)

    def test_drink_init_(self):
        name = "nz"
        portion = 500
        brand = "nz"
        drink = Water(name, portion, brand)
        self.assertEqual(name, drink.name)
        self.assertEqual(portion, drink.portion)
        self.assertEqual(brand, drink.brand)
        self.assertEqual(1.5, drink.price)

    def test_drink_name_setter(self):
        name = "test"
        portion = 500
        brand = "   "
        with self.assertRaises(ValueError) as ex:
            drink = Water(name, portion, brand)
        self.assertEqual("Brand cannot be empty string or white space!", str(ex.exception))

    def test_table_init(self):
        table_number = 101
        capacity = 10
        table = OutsideTable(table_number, capacity)
        self.assertEqual(table_number, table.table_number)
        self.assertEqual(capacity, table.capacity)
        self.assertEqual([], table.food_orders)
        self.assertEqual([], table.drink_orders)
        self.assertEqual(0, table.number_of_people)
        self.assertFalse(table.is_reserved)

    def test_get_bill(self):
        name = "nz"
        portion = 500
        brand = "nz"
        drink = Water(name, portion, brand)
        table_number = 67
        capacity = 10
        table = OutsideTable(table_number, capacity)
        table.reserve(1)
        table.order_drink(drink)
        table.order_drink(drink)
        self.assertEqual([drink, drink], table.drink_orders)
        self.assertTrue(table.is_reserved)
        self.assertEqual(1, table.number_of_people)
        table.clear()
        self.assertEqual([], table.drink_orders)
        self.assertEqual(0, table.number_of_people)
        self.assertFalse(table.is_reserved)

    def test_free_table_info(self):
        table_number = 67
        capacity = 10
        table = OutsideTable(table_number, capacity)
        result = table.free_table_info()
        exp_result = f"Table: {table.table_number}\nType: {table.__class__.__name__}\nCapacity: {table.capacity}"
        self.assertEqual(exp_result, result)


if __name__ == '__main__':
    unittest.main()

