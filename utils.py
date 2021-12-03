"""
Module provides classes and functions for working
with students.json & rooms.json
(reading, merging, creating output file).
"""


import argparse
import json
from dataclasses import dataclass
import xml.etree.cElementTree as ET


def read_input_arguments() -> tuple:
    """
    Reads and returns user's input arguments (absolute paths for
    students.json & rooms.json, expected output format for
    a resulted file.
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
    :type item_converter: function
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

    @property
    def merged(self) -> dict:
        """
        Provides dict with rooms data extended with students data.
        """
        data = {room.id: {'name': room.name, 'students': {}} for room in self.rooms}
        for student in self.students:
            data[student.room]['students'].update({student.id: student.name})
        return data


def create_json_output_file(data: dict):
    """
    Creates output JSON file with resulted dict of rooms with students.
    """
    with open('rooms_with_students.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def create_xml_output_file(data: dict):
    """
    Creates output XML file with resulted dict of rooms with students.
    """
    root = ET.Element('rooms')
    for room_id, room_data in data.items():
        room = ET.SubElement(root, 'room', id=str(room_id))
        room_name = ET.SubElement(room, 'name')
        room_name.text = room_data['name']
        for student_id, student_name in room_data['students'].items():
            student = ET.SubElement(room, 'student', id=str(student_id))
            student.text = student_name
    rooms = ET.ElementTree(root)
    ET.indent(rooms, space='\t', level=0)
    with open('rooms_with_students.xml', 'wb') as file:
        rooms.write(file, xml_declaration=False, encoding='utf-8')
