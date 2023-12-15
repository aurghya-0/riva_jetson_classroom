from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb+srv://aurghyadip:aurghya@whispertranscriptions.lmeavmb.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['transcriptionList']


def get_collection(collection_name):
    db = get_database()
    collection = db[collection_name]
    return collection
