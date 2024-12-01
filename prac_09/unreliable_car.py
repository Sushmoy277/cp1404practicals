# import random
# from prac_09.car import Car
#
#
# class UnreliableCar(Car):
#     """A car that may or may not drive, depending on its reliability."""
#
#     def __init__(self, name, fuel, reliability):
#         """Initialise an UnreliableCar instance, based on parent class Car."""
#         super().__init__(name, fuel)  # Call the parent class (Car) __init__ method
#         self.reliability = reliability  # Set the reliability attribute
#
#     def drive(self, distance):
#         """Drive the car based on its reliability."""
#         # Generate a random number between 0 and 100
#         random_number = random.randint(0, 100)
#
#         # If the random number is less than the reliability, drive the car
#         if random_number < self.reliability:
#             return super().drive(distance)  # Call the parent class's drive method
#         else:
#             return 0  # Car didn't drive, return 0 km driven
"""
CP1404/CP5632 Practical - Suggested Solution
UnreliableCar class, derived from Car
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        # Either way, we want to call the parent class's drive method (maybe driving 0)
        distance_driven = super().drive(distance)
        return distance_driven