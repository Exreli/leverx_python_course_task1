"""
Module provides classes and functions for working
with students.json & rooms.json
(reading, merging, creating output file).
"""


import argparse
import json
from dataclasses import dataclass
import os.path
import xml.etree.cElementTree as ET


def read_input_arguments():
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
    if not os.path.exists(args.students):
        raise FileNotFoundError("Got non-existent path for students.json")
    elif not os.path.exists(args.rooms):
        raise FileNotFoundError("Got non-existent path for rooms.json")
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


def read_students_from_json(path):
    """
    Opens students.json by its absolute path and loads its data.
    :param path: absolute path for students.json
    :type path: str

    :return: list of Student instances
    """
    with open(path, encoding='utf-8') as file:
        students = [Student(id=item['id'], name=item['name'], room=item['room'])
                    for item in json.load(file)]
    return students


def read_rooms_from_json(path):
    """
    Opens rooms.json by its absolute path and loads its data.
    :param path: absolute path for rooms.json
    :type path: str

    :return: list of Room instances
    """
    with open(path, encoding='utf-8') as file:
        rooms = [Room(id=item['id'], name=item['name']) for item in json.load(file)]
    return rooms


def merge_students_with_rooms(students, rooms):
    """
    Creates dict with rooms data extended with data of students.
    :param students:
    :param rooms:
    :return:
    """
    rooms_with_students = {room.id: {'name': room.name, 'students': {}} for room in rooms}
    for student in students:
        rooms_with_students[student.room]['students'].update({student.id: student.name})
    return rooms_with_students


def create_json_output_file(data):
    """
    Creates output JSON file with resulted dict of rooms with students.
    :param data: dict of rooms with students
    :type data: dict
    """
    with open('rooms_with_students.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def create_xml_output_file(data):
    """
    Creates output XML file with resulted dict of rooms with students.
    :param data: dict of rooms with students
    :type data: dict
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
