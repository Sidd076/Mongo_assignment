import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Employees"]

with open('data.json') as f:
    data = json.load(f)

details_collection = db["details"]
details_collection.insert_many(data)

client.close()
