import os
import csv


def read_file(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as file:
        return [row for row in csv.reader(file) if row]


def append_csv(path, row):
    file_exists = os.path.exists(path)

    with open(path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(path) == 0:
            writer.writerow(row.keys())

        writer.writerow(row.values())
