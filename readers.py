"""
Module provides classes and functions for reading user's input,
loading JSON files and working with its data.
"""


import argparse
import json
from dataclasses import dataclass


def read_input_arguments() -> tuple:
    """
    Reads and returns user's input arguments (absolute paths for
    JSON files and expected output format for the resulted file).
    """
    parser = argparse.ArgumentParser(
        description='Merging 2 JSON files and unloading it to JSON or XML file'
    )
    parser.add_argument('students', type=str, help='Absolute path for students.json')
    parser.add_argument('rooms', type=str, help='Absolute path for rooms.json')
    parser.add_argument('format', type=str, choices=['JSON', 'XML'],
                        help='Expected output format (JSON or XML)')
    args = parser.parse_args()
    return args.students, args.rooms, args.format


@dataclass()
class Student:
    """
    Class for working with students.json data
    """
    id: int
    name: str
    room: int


@dataclass()
class Room:
    """
    Class for working with rooms.json data
    """
    id: int
    name: str


def load_data_from_json(path: str, item_converter) -> list:
    """
    Opens JSON file by its absolute path and loads its data.

    :param path: absolute path for JSON file

    :param item_converter: lambda constructor
    :type item_converter: func
    """
    with open(path, encoding='utf-8') as file:
        data = [item_converter(item) for item in json.load(file)]
    return data


class RoomsStudents:
    """
    Class for working with merged students & rooms data.
    """
    def __init__(self, students: list, rooms: list):
        """
        Creates a new RoomsStudents object with given students & rooms data.
        """
        self.students = students
        self.rooms = rooms

    def get_merged_data(self) -> dict:
        """
        Provides dict with rooms data extended with students data.
        """
        data = {room.id: {'name': room.name, 'students': {}} for room in self.rooms}
        for student in self.students:
            data[student.room]['students'].update({student.id: student.name})
        return data
