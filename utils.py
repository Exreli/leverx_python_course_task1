"""
Module provides classes for working
with students.json & rooms.json
(reading, merging, creating output file).
"""

import json
import xmltodict


class Rooms:
    """
    Class for working with rooms.json data.
    """
    def __init__(self, path):
        """
        Reads data from rooms.json.

        :param path: absolute path to file in file system
        :type path: str
        """
        with open(path, encoding='utf-8') as file:
            self.data = json.load(file)


class Students(Rooms):
    """
    Class for working with students.json data.
    Reading data from file is same as for rooms.json.
    """
    @staticmethod
    def check_for_room(other):
        """
        Check if object belongs to Rooms class.

        :param other: object to check
        :return: boolean
        """
        return isinstance(other, Rooms)

    def merge(self, other):
        """
        Merges data from Students and Rooms,
        extends contain of Rooms data dict
        with Students data dict.

        :param other: object of Rooms class
        :type other: Rooms

        :raises ValueError: if other is not instance of Rooms

        :return: list of rooms with students
        """
        if Students.check_for_room(other):
            output_data = other.data.copy()
            for student in self.data:
                student_no_room = student.copy()
                del student_no_room['room']
                output_data[student['room']]['students'] =\
                    output_data[student['room']].get('students', []) + [student_no_room]
            return output_data
        else:
            raise ValueError('Room expected')


class Output:
    """
    Class for working with resulted list of rooms with students,
    provides ability of creating output JSON/XML file with its data.
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
        Provides creating output JSON/XML file
        with list of rooms with students.
        """
        if self.format == 'JSON':
            with open('output.json', 'w', encoding='utf-8') as file:
                json.dump(self.output_data, file, indent=4)
        else:
            with open('output.xml', 'w', encoding='utf-8') as file:
                xmltodict.unparse({'Rooms': self.output_data}, output=file,
                                  pretty=True, full_document=False)
