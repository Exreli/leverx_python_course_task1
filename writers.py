"""
Module provides classes for creating XML and JSON output files
with resulted data.
"""


import json
import xml.etree.cElementTree as ET


class JsonSerializer:
    """
    Class for serializing given data to a JSON formatted string.
    """
    def __init__(self, data: dict):
        self.data = data
        self.serialized_data = self.serialize()

    def serialize(self) -> str:
        """
        Serializes data to a JSON formatted string and returns it.
        """
        return json.dumps(self.data, indent=4)


class JsonOutputFileWriter:
    """
    Class for creating an output JSON file with resulted data.
    """
    def __init__(self, data: str, path=r'output\output.json', encoding='utf-8'):
        """
        Creates a new JSONOutputFileWriter object with given data, path and encoding.
        By default the path to output file is 'output/output.json' in the current
        directory, encoding - utf-8.
        """
        self.data = data
        self.path = path
        self.encoding = encoding

    def create(self):
        """
        Creates an output JSON file with resulted data.
        """
        with open(self.path, 'w', encoding=self.encoding) as file:
            json.dump(json.loads(self.data), file, indent=4)


class XmlSerializer:
    """
    Class for serializing given data to an XML formatted ElementTree object.
    """
    def __init__(self, data: dict):
        self.data = data
        self.serialized_data = self.serialize()

    def serialize(self) -> 'ET.ElementTree':
        """
        Serializes data to an XML formatted ElementTree object and returns it.
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
        ET.indent(element_tree, space='\t', level=0)
        return element_tree


class XmlOutputFileWriter:
    """
    Class for creating an output XML file with resulted data.
    """
    def __init__(self, data: 'ET.ElementTree', path=r'output\output.xml', encoding='utf-8'):
        """
        Creates a new XMLOutputFileWriter object with given data, path and encoding.
        By default the path to output file is 'output/output.xml' in the current
        directory, encoding - utf-8.
        """
        self.data = data
        self.path = path
        self.encoding = encoding

    def create(self):
        """
        Creates an output XML file with resulted data.
        """
        with open(self.path, 'wb') as file:
            self.data.write(file, xml_declaration=False, encoding=self.encoding)
