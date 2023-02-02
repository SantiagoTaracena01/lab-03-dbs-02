import csv
import json

def csv_to_json(csv_path, json_path):
    json_array = []

    with open(csv_path, encoding='utf-8') as csv_file: 
        csv_reader = csv.DictReader(csv_file) 
        for row in csv_reader: 
            json_array.append(row)

    with open(json_path, 'w', encoding='utf-8') as json_file: 
        json_string = json.dumps(json_array, indent=4)
        json_file.write(json_string)
