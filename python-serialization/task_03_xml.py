#!/usr/bin/env python3
"""Serializing and Deserializing with XML as an alternative to JSON"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary: A Python dictionary to serialize
        filename: The filename to save the XML data
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file and return a Python dictionary.

    Args:
        filename: The filename of the XML file to read

    Returns:
        A Python dictionary with the deserialized data
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
