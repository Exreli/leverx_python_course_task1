"""
Script for reading 2 JSON files (students.json, rooms.json),
merging them and creating new JSON/XML file.
"""

from utils import *


def main():
    """
    Reads user's input arguments
    """
    students_path, rooms_path, output_format = read_input_arguments()
    students = load_data_from_json(
        students_path,
        lambda item: Student(id=item['id'], name=item['name'], room=item['room']))
    rooms = load_data_from_json(
        rooms_path, lambda item: Room(id=item['id'], name=item['name']))
    rooms_students = RoomsStudents(students, rooms)
    output_dict = {'JSON': create_json_output_file, 'XML': create_xml_output_file}
    output_dict[output_format](rooms_students.merged)


if __name__ == "__main__":
    main()
