"""
Module provides functions for reading user's input
and loading JSON files.
"""


import argparse
import json


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
