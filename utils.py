import json


class Rooms:
    def __init__(self, path):
        with open(path, encoding='utf-8') as file:
            self.data = json.load(file)


class Students(Rooms):
    @staticmethod
    def check_for_room(rooms):
        return isinstance(rooms, Rooms)

    def merge(self, rooms):
        if Students.check_for_room(rooms):
            output_data = rooms.data.copy()
            for student in self.data:
                student_no_room = student.copy()
                del student_no_room['room']
                output_data[student['room']]['students'] =\
                    output_data[student['room']].get('students', []) + [student_no_room]
            return output_data
        else:
            raise ValueError('Room expected')