from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus("doadmin")
password = urllib.parse.quote_plus("0PG12W983Ier7b4R")

cluster = MongoClient(
    # "mongodb+srv://Kirill:bjObxVisIWqE0Gyr@cluster0.5m5xlod.mongodb.net/?retryWrites=true&w=majority")
    "mongodb+srv://%s:%s@tempusdata-67ad90d4.mongo.ondigitalocean.com" % (username, password))

db = cluster["IndividualDataDB"]
collection = db["Auth"]

# Securit
