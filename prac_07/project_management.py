"""
Project Management System
Estimate: 2 hours
Actual:   3 hours
"""
from project import Project
import datetime

MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> """


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects()

    choice = input(MENU).upper().strip()  # Get the initial menu choice
    while choice != 'Q':
        if choice == 'L':
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            projects.append(add_new_project())
        elif choice == 'U':
            update_project(projects)
        else:
            print("Invalid menu choice")

        choice = input(MENU).upper().strip()

    save_choice = input("Would you like to save to projects.txt? (y/n): ").lower().strip()
    if save_choice == 'y':
        save_projects("projects.txt", projects)
        print(f"{len(projects)} projects saved to projects.txt")
        print("Thank you for using custom-built project management software.")
    else:
        print("Thank you for using custom-built project management software.")


def load_projects(filename="projects.txt"):
    projects = []
    with open(filename, 'r') as file:
        file.readline()
        for line in file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = parts[2]
            estimate = parts[3]
            completion = parts[4]
            project = Project(name, start_date, priority, estimate, completion)
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(project.to_line() + "\n")
    print(f"Saved {len(projects)} projects to {filename}")


def get_priority(project):
    return project.priority


def get_start_date(project):
    return project.start_date


def display_projects(projects):
    incomplete_projects = sorted([p for p in projects if not p.is_complete()], key=get_priority)
    complete_projects = sorted([p for p in projects if p.is_complete()], key=get_priority)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > filter_date]

    # Sort the filtered projects by the start_date using the get_start_date function
    sorted_filtered_projects = sorted(filtered_projects, key=get_start_date)
    for project in sorted_filtered_projects:
        print(f"  {project}")


def add_new_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, estimate, completion)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    new_completion = input("New Percentage: ")
    if new_completion:
        project['completion'] = int(new_completion)

    new_priority = input("New Priority: ")
    if new_priority:
        project['priority'] = int(new_priority)


if __name__ == "__main__":
    main()
