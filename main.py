import argparse

parser = argparse.ArgumentParser(description="Merging 2 JSON files to one list and unloading it to JSON or XML")
parser.add_argument('students', type=str, help='Input dir for students JSON')
parser.add_argument('rooms', type=str, help='Input dir for rooms JSON')
parser.add_argument('format', type=str, choices=['JSON', 'XML'], help='Output format (JSON or XML)')
args = parser.parse_args()

