present_year = 2024
vintage_age = 50
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost
    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
    def get_age(self):
        return present_year - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= vintage_age

