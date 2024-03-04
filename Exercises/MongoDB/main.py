
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://s0533115692:kAtP4GkG0NmDSVoX@test.0bd2tuc.mongodb.net/?retryWrites=true&w=majority&appName=test"

# Create a new client and connect to the server
client = MongoClient(uri)