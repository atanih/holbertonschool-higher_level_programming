#!/usr/bin/env python3
"""Converting CSV Data to JSON Format using serialization techniques"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and save it to data.json.

    Args:
        csv_filename: The filename of the input CSV file

    Returns:
        True if conversion was successful, False otherwise
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
