"""
Concept: Factory Pattern

The Factory pattern provides an interface for creating objects without specifying
their exact class. A factory function/method decides which class to instantiate
based on input parameters.

When to use:
- When you have multiple classes with a common interface
- When the creation logic is complex
- When you want to decouple object creation from usage
- When you might add new types in the future

Example:
```python
class Circle:
    def draw(self):
        return "Drawing a circle"

class Square:
    def draw(self):
        return "Drawing a square"

def shape_factory(shape_type):
    '''Factory function that creates shapes'''
    if shape_type == "circle":
        return Circle()
    elif shape_type == "square":
        return Square()
    else:
        raise ValueError(f"Unknown shape: {shape_type}")

# Usage:
shape = shape_factory("circle")
print(shape.draw())  # "Drawing a circle"
```

Benefits:
- Adding new shapes doesn't change the client code
- Creation logic is centralized
- Easy to test (can mock the factory)

Task:
Complete the `vehicle_factory` function to:
1. Return a Car instance when vehicle_type is "car"
2. Return a Motorcycle instance when vehicle_type is "motorcycle"
3. Raise ValueError for unknown vehicle types
"""


class Vehicle:
    """Base class for all vehicles"""

    def start(self):
        raise NotImplementedError


class Car(Vehicle):
    def start(self):
        return "Car engine starting: Vroom!"

    def honk(self):
        return "Beep beep!"


class Motorcycle(Vehicle):
    def start(self):
        return "Motorcycle engine starting: Brap brap!"

    def honk(self):
        return "Meep meep!"


def vehicle_factory(vehicle_type):
    """
    Factory function that creates vehicles based on type string.

    Args:
        vehicle_type: Either "car" or "motorcycle"

    Returns:
        A Vehicle instance (Car or Motorcycle)

    Raises:
        ValueError: If vehicle_type is not recognized
    """
    # TODO: Implement the factory logic
    # 1. If vehicle_type == "car", return a Car()
    # 2. If vehicle_type == "motorcycle", return a Motorcycle()
    # 3. Otherwise, raise ValueError with a helpful message

    # FIX ME: Return the correct vehicle based on vehicle_type
    pass


def main():
    # Test 1: Factory creates Car
    car = vehicle_factory("car")

    if car is None:
        raise Exception(
            "vehicle_factory('car') returned None!\n"
            "Hint: Return Car() when vehicle_type == 'car'"
        )

    if not isinstance(car, Car):
        raise Exception(
            f"Expected Car instance, got {type(car).__name__}\n"
            "Hint: Check if vehicle_type == 'car' and return Car()"
        )

    if car.start() != "Car engine starting: Vroom!":
        raise Exception("Car.start() returned wrong message")

    # Test 2: Factory creates Motorcycle
    moto = vehicle_factory("motorcycle")

    if moto is None:
        raise Exception(
            "vehicle_factory('motorcycle') returned None!\n"
            "Hint: Return Motorcycle() when vehicle_type == 'motorcycle'"
        )

    if not isinstance(moto, Motorcycle):
        raise Exception(f"Expected Motorcycle instance, got {type(moto).__name__}")

    # Test 3: Factory raises ValueError for unknown types
    try:
        vehicle_factory("helicopter")
        raise Exception(
            "vehicle_factory('helicopter') should raise ValueError!\n"
            "Hint: Add an else clause that raises ValueError"
        )
    except ValueError:
        pass  # Correct!

    # Test 4: Different calls create different instances
    car1 = vehicle_factory("car")
    car2 = vehicle_factory("car")
    if car1 is car2:
        raise Exception(
            "Factory should create NEW instances each time!\n"
            "Hint: Return Car(), not a stored instance"
        )

    print("Factory pattern working correctly!")


if __name__ == "__main__":
    main()
