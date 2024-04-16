from csv import reader
from json import dump
from os import path


def csv_to_json(csv_file_path: str, json_file_path: str) -> None:
    if not path.exists(csv_file_path):
        raise FileNotFoundError

    rows = []

    with open(csv_file_path, 'r') as csv_file:
        for row in reader(csv_file):
            rows.append(row)

    if rows == []:
        raise FileNotFoundError("Empty file")

    headers = rows[0]
    values = rows[1:]

    objects = []

    for i in range(len(values)):
        object_ = {}
        for j in range(len(headers)):
            object_[headers[j]] = values[i][j]
        objects.append(object_)

    if path.exists(json_file_path):
        raise FileExistsError

    with open(json_file_path, 'w') as json_file:
        dump(objects, json_file, indent=4)
