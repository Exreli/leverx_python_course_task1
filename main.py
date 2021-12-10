"""
Script for reading 2 JSON files,
merging their data and creating new JSON/XML file.
"""


from models import Student, Room, RoomsStudents
from readers import read_input_arguments, load_data_from_json


def main():
    """
    Main script's function.
    1. Reads user's input arguments.
    2. Loads data from JSON files.
    3. Merges both JSON files' data.
    4. Creates output file with the resulted data.
    """
    students_path, rooms_path, output_format, output_formats = read_input_arguments()
    students = load_data_from_json(
        students_path,
        lambda item: Student(id=item['id'], name=item['name'], room=item['room'])
    )
    rooms = load_data_from_json(
        rooms_path, lambda item: Room(id=item['id'], name=item['name'])
    )
    rooms_students = RoomsStudents(students, rooms)
    merged_data = rooms_students.get_merged_data()
    serialized_data = output_formats[output_format]['serialize'](merged_data).serialized_data
    output_file_creator = output_formats[output_format]['create'](serialized_data)
    output_file_creator.create()


if __name__ == "__main__":
    main()
