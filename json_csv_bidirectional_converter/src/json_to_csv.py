from csv import writer
from json import load
from os import path


def json_to_csv(json_file_path, csv_file_path) -> None:
    if not path.exists(json_file_path):
        raise FileNotFoundError

    with open(json_file_path, 'r') as json_file:
        objects = load(json_file)

    if not objects:
        raise FileNotFoundError("Empty file")

    rows = []

    headers = list(objects[0].keys())
    rows.append(headers)

    for object_ in objects:
        values = list(object_.values())
        rows.append(values)

    if path.exists(csv_file_path):
        raise FileExistsError

    with open(csv_file_path, 'w') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerows(rows)
