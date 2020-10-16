
from xml.etree import ElementTree as ET


class XMLParser:

    @staticmethod
    def get_root(data):
        tree = ET.parse(data)
        return tree.getroot()

    @staticmethod
    def get_node(parent, pattern=''):
        return parent.find('.//{}'.format(pattern))

    @staticmethod
    def get_text(node):
        return node.text

    @staticmethod
    def get_attr(node, pattern):
        return node.attrib.get(pattern)
