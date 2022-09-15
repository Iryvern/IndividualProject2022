from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://Kirill:bjObxVisIWqE0Gyr@cluster0.5m5xlod.mongodb.net/?retryWrites=true&w=majority")

db = cluster["DataDB"]
collection = db["Individual2022"]


def add_data(data):
    collection.insert_one(data)
