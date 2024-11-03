"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language client code.
"""
"""
Word Occurrences
Estimate: 30 minutes
Actual:   15 minutes 
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages_list = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages_list:
        if language.is_dynamic():
            print(language.name)


main()
