"""
Module provides classes for working with
data read from JSON files.
"""


from dataclasses import dataclass


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
