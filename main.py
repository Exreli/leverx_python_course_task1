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
    students = read_students_from_json(students_path)
    rooms = read_rooms_from_json(rooms_path)
    rooms_with_students = merge_students_with_rooms(students, rooms)
    output_dict = {'JSON': create_json_output_file, 'XML': create_xml_output_file}
    output_dict[output_format](rooms_with_students)


if __name__ == "__main__":
    main()
