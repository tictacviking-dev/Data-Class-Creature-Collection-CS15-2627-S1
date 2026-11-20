from dataclasses import dataclass

@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float

creature1 = Creature("owen", "pig", 12, 150.5)
creature2 = Creature("ridhay", "ape", 5, 60.0)
creature3 = Creature("Mr.Forsyth", "lion", 8, 45.5)
print("Creature 1")
print("Name:", creature1.name)
print("Species:", creature1.species)
print("Level:", creature1.level)
print("Health:", creature1.health)
print()
print("Creature 2")
print("Name:", creature2.name)
print("Species:", creature2.species)
print("Level:", creature2.level)
print("Health:", creature2.health)
print()
print("Creature 3")
print("Name:", creature3.name)
print("Species:", creature3.species)
print("Level:", creature3.level)
print("Health:", creature3.health)
print()
creature2.level = 6
creature2.health = 75.5
print("Creature 2 after changes")
print("Name:", creature2.name)
print("Species:", creature2.species)
print("Level:", creature2.level)
print("Health:", creature2.health)
print()
print("Creature 1 still has level", creature1.level, "and health", creature1.health)
print("Creature 3 still has level", creature3.level, "and health", creature3.health)