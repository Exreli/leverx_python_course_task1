"""
Script for reading 2 JSON files (students.json, rooms.json),
merging them into list of rooms with students
and creating new JSON/XML file with resulted list.
"""

import argparse
from utils import JSONData, Output

parser = argparse.ArgumentParser(description='Merging 2 JSON files to one list and '
                                             'unloading it to JSON or XML')
parser.add_argument('students', type=str, help='Input dir for students JSON')
parser.add_argument('rooms', type=str, help='Input dir for rooms JSON')
parser.add_argument('format', type=str, choices=['JSON', 'XML'], help='Output format (JSON or XML)')
args = parser.parse_args()

input_data = JSONData(args.students, args.rooms)
output = Output(args.format, input_data.merge_data())
output.output()
