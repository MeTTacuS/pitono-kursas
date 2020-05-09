from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client.database
inv = database["inventory"]

def query1():
  entries = inv.find()
  for entry in entries:
    print(entry)

def query2():
  entries = inv.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1})
  for entry in entries:
    print(entry)

def query3():
  entries = inv.find({}, {"_id": 0, "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1})
  for entry in entries:
    print(entry)

def query4():
  entries = inv.find({"borough": "Bronx"})
  for entry in entries:
    print(entry)

def query5():
  entries = inv.find({"grades": {"$elemMatch": {"score": {"$gte": 80, "$lte": 100}}}})
  for entry in entries:
    print(entry)
