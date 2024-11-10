from prac_06.guitar import Guitar
present_year = 2024


def run_tests():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2013, 1000.00)

    print(f"{guitar1.name} get_age() - Expected {100}. Got {guitar1.get_age()}")
    print(f"{other.name} get_age() - Expected {9}. Got {other.get_age()}")
    print()
    print(f"{guitar1.name} is_vintage() - Expected {True}. Got {guitar1.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


if __name__ == '__main__':
    run_tests()