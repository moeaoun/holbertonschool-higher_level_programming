#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    # Create the root element
    root = ET.Element("data")
    
    # Add dictionary elements as child elements to the root
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Ensure the value is converted to a string

    # Create an ElementTree object from the root and write to the file
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary."""
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Convert XML elements into a dictionary
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None

