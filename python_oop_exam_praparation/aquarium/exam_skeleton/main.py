from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.controller import Controller
from project.fish.saltwater_fish import SaltwaterFish
#
aquarium = Controller()
print(aquarium.add_aquarium("FreshwaterAquarium", "test"))
print(aquarium.add_decoration("Plant"))
print(aquarium.calculate_value("test"))
print(aquarium.add_fish("test", "FreshwaterFish", "nz", "nz", 12))
print(aquarium.calculate_value("test"))

print(aquarium.report())
print(aquarium.feed_fish("test"))

aquarium.feed_fish("test")
for aquarium in aquarium.aquariums:
    for fish in aquarium.fish:
        print(fish.size)