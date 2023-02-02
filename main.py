import os
import json
import pymongo
from dotenv import load_dotenv
from csv_to_json import csv_to_json

csv_file_path = r"./data/winemag-data.csv"
json_file_path = r"./data/winemag-json.json"

csv_to_json(csv_file_path, json_file_path)

load_dotenv()

CONNECTION_STRING = os.getenv("CONNECTION_STRING")

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.lab03
winemag = db.winemag

with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    for document in data:
        winemag.insert_one(document)
