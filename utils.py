"""
Module provides classes for working
with students.json & rooms.json
(reading, merging, creating output file).
"""

import json
import xmltodict


class JSONData:
    """
    Class for reading and merging data
    from JSON files (students.json, rooms.json).
    """
    def __init__(self, students_path, rooms_path):
        """
        Opens students.json & rooms.json by its absolute paths
        and loads its data to dicts.

        :param students_path: absolute path to students.json in file system
        :type students_path: str

        :param rooms_path: absolute path to rooms.json in file system
        :type rooms_path: str
        """
        with open(students_path, encoding='utf-8') as students, \
                open(rooms_path, encoding='utf-8') as rooms:
            self.students = json.load(students)
            self.rooms = json.load(rooms)

    def merge_data(self):
        """
        Extends rooms.json data dict with
        students.json data dict

        :return: list of rooms with students
        """
        merged_data = self.rooms.copy()
        for student in self.students:
            student_no_room = student.copy()
            del student_no_room['room']
            merged_data[student['room']]['students'] = \
                merged_data[student['room']].get('students', []) + [student_no_room]
        return merged_data


class Output:
    """
    Class for creating output JSON/XML file
    with resulted list of rooms with students.
    """
    def __init__(self, output_format, output_data):
        """
        :param output_format: Expected format of output file (JSON, XML)
        :type output_format: str

        :param output_data: list of rooms with students
        :type output_data: list
        """
        self.format = output_format
        self.output_data = output_data

    def output(self):
        """
        Creates output JSON/XML file
        with list of rooms with students.
        """
        if self.format == 'JSON':
            with open('output.json', 'w', encoding='utf-8') as file:
                json.dump(self.output_data, file, indent=4)
        else:
            with open('output.xml', 'w', encoding='utf-8') as file:
                xmltodict.unparse({'Rooms': self.output_data}, output=file,
                                  pretty=True, full_document=False)
