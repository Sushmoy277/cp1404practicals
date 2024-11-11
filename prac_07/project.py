"""
Project Management System

Estimate: 2 hours
Actual:   3 hours
"""

import datetime


class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.estimate = float(estimate)
        self.completion = int(completion)

    def is_complete(self):
        return self.completion == 100

    def update(self, completion=None, priority=None):
        if completion is not None:
            self.completion = completion
        if priority is not None:
            self.priority = priority

    def to_line(self):
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.estimate:.2f}\t{self.completion}"

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"
