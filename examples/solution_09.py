from datetime import datetime

from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        documents = biographies.find({"awards": {"$elemMatch": {"award": {"$regex": "Science"}}}})

        for document in documents:
            print(document)

        documents = biographies.find({"awards": {"$elemMatch": {"year": 2001}}})

        for document in documents:
            print(document)