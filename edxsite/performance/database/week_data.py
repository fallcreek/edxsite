import pickle
import os
import json
from pymongo import MongoClient
client = MongoClient()

db = client.edx
collection = db.week_problem

my_path = os.path.abspath(os.path.dirname(__file__))


file_path = "/data/week_pkl/Week7_data.pkl"
path = my_path + file_path

week_data = pickle.load(open(path, 'rb'))

for key in week_data:
    print(key)
    json_str = json.dumps(week_data[key])
    json_obj = json.loads(json_str)
    print(json_obj)
    collection.insert(json_obj)


