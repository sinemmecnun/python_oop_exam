from project.bakery import Bakery

bakery = Bakery("Test")
print(bakery.add_food("Bread", "nz", 12))
print(bakery.food_menu)
print(bakery.add_drink("Tea", "nz", 12, "nz"))
print(bakery.drinks_menu)
print(bakery.add_table("InsideTable", 12, 10))
print(bakery.add_table("InsideTable", 11, 10))
print(bakery.reserve_table(10))
print(bakery.order_food(12, "mleko", "nz"))
print(bakery.order_drink(12, "nz", "chay"))
print(bakery.get_total_income())
print(bakery.get_free_tables_info())


