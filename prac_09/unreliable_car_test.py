# from prac_09.unreliable_car import UnreliableCar
#
#
# def main():
#     """Test the UnreliableCar class."""
#     # Create an UnreliableCar instance with a 50% chance of driving
#     my_car = UnreliableCar("Old Rusty", 100, 50)
#
#     # Try driving the car for 20 km
#     distance_driven = my_car.drive(20)
#
#     # Print the result
#     print(f"Attempted to drive 20 km, the car drove {distance_driven} km.")
#
#     # Try driving the car again
#     distance_driven = my_car.drive(50)
#
#     # Print the result again
#     print(f"Attempted to drive 50 km, the car drove {distance_driven} km.")
#
#
# # Call the main function to run the test
# main()
"""
CP1404/CP5632 Practical - Suggested Solution
UnreliableCar class tests

The point to an UnreliableCar is that it randomly does not always drive.
So, these tests run several times in order to see that randomness.
We expect the good car (high reliability) to drive more often than the bad car.
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    # create cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()