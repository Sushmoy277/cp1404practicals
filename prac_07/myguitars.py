import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main program to manage guitars."""
    guitars = load_guitars(FILENAME)

    # Display all guitars
    print("These are the guitars currently in the list:")
    for guitar in guitars:
        print(guitar)

    # Sort guitars by year and display them in sorted order
    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    # Add new guitars from user input
    guitars = add_guitars(guitars)

    # Save all guitars back to the file
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def add_guitars(guitars):
    """Prompt user to add new guitars and return the updated list."""
    print("\nAdd new guitars (leave the name blank to stop):")
    adding_guitars = True
    while adding_guitars:
        name = input("Name: ")
        if name == "":  # Exit loop if the user enters a blank name
            adding_guitars = False
        else:
            year = int(input("Year: "))
            cost = float(input("Cost: $ "))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"Added {new_guitar}")
    return guitars


if __name__ == "__main__":
    main()
