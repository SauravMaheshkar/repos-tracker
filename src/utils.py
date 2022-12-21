"""Utility functions for serializing data to JSON files."""
import json


def write_to_json(file_name: str, data: list) -> None:
    """
    Serialize a list of data to a JSON file.

    :param file_name: The name of the file to write to.
    :type file_name: str
    :param data: The data to serialize.
    :type data: list
    :return: None
    """
    try:
        with open(file=file_name, mode="x", encoding="utf8") as json_file:
            json.dump(data, json_file)
    except FileExistsError:
        with open(file=file_name, mode="w", encoding="utf8") as json_file:
            json.dump(data, json_file)
