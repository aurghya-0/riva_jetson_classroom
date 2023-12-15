from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb://127.0.0.1:27017/classroom"
    client = MongoClient(CONNECTION_STRING)
    return client['transcriptionList']


def get_collection(collection_name):
    db = get_database()
    collection = db[collection_name]
    return collection
