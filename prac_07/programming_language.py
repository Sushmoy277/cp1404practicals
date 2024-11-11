"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection},"
                f"Pointer Arithmetic={self.pointer_arithmetic},"
                f" First appeared in {self.year}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    java = ProgrammingLanguage("Java", "Static", True, 1995, False)
    cpp = ProgrammingLanguage("C++", "Static", False, 1983, True)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    go = ProgrammingLanguage("Go", "Static", True, 2009, False)
    swift = ProgrammingLanguage("Swift", "Static", True, 2014, False)
    rust = ProgrammingLanguage("Rust", "Static", False, 2010, True)

    languages = [java, cpp, python, visual_basic, ruby, go, swift, rust]
    print("All programming languages:")
    for language in languages:
        print(language)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
