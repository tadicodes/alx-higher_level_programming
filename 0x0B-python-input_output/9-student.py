#!/usr/bin/python3
"""student to JSON"""


class Student:
    """representation of a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation of a Student instance"""
        return self.__dict__
