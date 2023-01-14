from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus("doadmin")
password = urllib.parse.quote_plus("0PG12W983Ier7b4R")


def key():
    return "ZOl9P^8Ag9K6O2JCmjc&"


cluster = MongoClient(
    "mongodb+srv://%s:%s@tempusdata-67ad90d4.mongo.ondigitalocean.com" % (username, password))

db = cluster["IndividualDataDB"]
collection = db["Auth"]

# Credentails need to be converted to .env and ignored, but the VM at the hosting service needs the data, the env can be generated in the pipeline
