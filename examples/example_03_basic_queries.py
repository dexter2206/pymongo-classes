import re
from datetime import datetime
from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        # Find everyone with name "John"
        documents = biographies.find({"name.first": "John"})

        print("> People named John:")
        for document in documents:
            print(document["name"]["first"], document["name"]["last"])

        # Find everyone with name starting with "J"
        documents = biographies.find({"name.first": {"$regex": "^J"}})

        print("> People whose name starts with J:")
        for document in documents:
            print(document["name"]["first"], document["name"]["last"])

        # Find everyone with name starting with "J" - alternative version
        # using Python's re module
        documents = biographies.find({"name.first": re.compile("^J")})

        print("> People whose name starts with J:")
        for document in documents:
            print(document["name"]["first"], document["name"]["last"])

        # Find everyone born before 1960
        documents = biographies.find({"birth": {"$lt": datetime(1960, 1, 1, 0, 0)}})

        print("> People born before 1960:")
        for document in documents:
            print(document["name"]["first"], document["name"]["last"])