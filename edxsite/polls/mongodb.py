from pymongo import MongoClient
import  pprint

client = MongoClient()

db = client.edx
collection = db.problem

for p in collection.find():
    print(str(p["week"]) + " " + str(p["problem"]))