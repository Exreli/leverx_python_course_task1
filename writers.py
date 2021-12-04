"""
Module provides classes for creating XML and JSON output files
with resulted data.
"""


import json
import xml.etree.cElementTree as ET


class JSONOutputFileWriter:
    """
    Class for creating output JSON file with resulted data.
    """
    def __init__(self, data: dict, path=r'output\output.json', encoding='utf-8'):
        """
        Creates a new JSONOutputFileWriter object with given data, path and encoding.
        By default the path to output file is 'output/output.json' in the current
        directory, encoding - utf-8.
        """
        self.data = data
        self.path = path
        self.encoding = encoding

    def create_file(self):
        """
        Creates output JSON file with resulted data.
        """
        with open(self.path, 'w', encoding=self.encoding) as file:
            json.dump(self.data, file, indent=4)


class XMLOutputFileWriter:
    """
    Class for building Element Trees by given resulted data and
    creating output XML file with it.
    """
    def __init__(self, data: dict, path=r'output\output.xml', encoding='utf-8'):
        """
        Creates a new XMLOutputFileWriter object with given data, path and encoding.
        By default the path to output file is 'output/output.xml' in the current
        directory, encoding - utf-8.
        """
        self.data = data
        self.path = path
        self.encoding = encoding

    def build_tree(self):
        """
        Builds Element Tree with the resulted data
        given to XMLOutputFileWriter object.
        """
        root = ET.Element('rooms')
        for room_id, room_data in self.data.items():
            room = ET.SubElement(root, 'room', id=str(room_id))
            room_name = ET.SubElement(room, 'name')
            room_name.text = room_data['name']
            for student_id, student_name in room_data['students'].items():
                student = ET.SubElement(room, 'student', id=str(student_id))
                student.text = student_name
        element_tree = ET.ElementTree(root)
        return element_tree

    def create_file(self):
        """
        Creates output XML file with resulted data.
        """
        element_tree = self.build_tree()
        ET.indent(element_tree, space='\t', level=0)
        with open(self.path, 'wb') as file:
            element_tree.write(file, xml_declaration=False, encoding=self.encoding)
