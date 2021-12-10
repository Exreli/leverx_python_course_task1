"""
Module provides functions for reading user's input
and loading JSON files.
"""


import argparse
import json
import writers
import inspect
import re


def get_available_output_formats(module=writers) -> dict:
    """
    Returns available output formats to create.
    Works correctly if all serializers and file-writers
    are implemented in module 'writers.py' and their names
    start with output format they work with, also serializers
    must have implemented method '.serialize(self)' and file-writers
    must have implemented method '.create(self)'.
    """
    output_formats = {}
    actions = ['serialize', 'create']
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            output_format = re.search(r'[A-Z][a-z]*', name).group(0).upper()
            for action in actions:
                if action in obj.__dict__:
                    output_formats[output_format] = output_formats.get(output_format, {}) | {action: obj}
    return output_formats


def read_input_arguments() -> tuple:
    """
    Reads and returns user's input arguments (absolute paths for
    JSON files and expected output format for the resulted file).
    """
    output_formats = get_available_output_formats()
    parser = argparse.ArgumentParser(
        description='Merging 2 JSON files and unloading it to JSON or XML file'
    )
    parser.add_argument('students', type=str, help='Absolute path for students.json')
    parser.add_argument('rooms', type=str, help='Absolute path for rooms.json')
    parser.add_argument('format', type=str, choices=output_formats,
                        help=f'Expected output format')
    args = parser.parse_args()
    return args.students, args.rooms, args.format, output_formats


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
