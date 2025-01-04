# Superhero class representing a superhero with unique attributes and methods
class Superhero:
    def __init__(self, name, superpower, strength_level):
        self.name = name
        self.superpower = superpower
        self.strength_level = strength_level

    def display_info(self):
        print(f"Superhero: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"Strength Level: {self.strength_level}")

    def save_the_day(self):
        print(f"{self.name} is using their {self.superpower} to save the day!")


# Example of creating a superhero object and calling methods
hero = Superhero("Captain Speed", "Super Speed", 90)
hero.display_info()
hero.save_the_day()


# Base class for Vehicle with a general move() method
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Car subclass that overrides the move() method
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane subclass that overrides the move() method
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat subclass that overrides the move() method
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Polymorphism in action
def vehicle_move(vehicle: Vehicle):
    vehicle.move()

# Example usage
car = Car()
plane = Plane()
boat = Boat()

# Calling the same method on different objects with different results
vehicle_move(car)   # Output: Driving 🚗
vehicle_move(plane) # Output: Flying ✈️
vehicle_move(boat)  # Output: Sailing ⛵
