from datetime import datetime

from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        # Find all people, but retrieve only name attribute.
        # Note that we need to supply query (in this case an empty dict)
        documents = biographies.find({}, {"name": 1})

        print("All people:")
        for document in documents:
            print(document)

        # Find all people born after 1957, retrieve only last name and birth date
        documents = biographies.find(
            {"birth": {"$gte": datetime(1958, 1, 1)}}, ["name.first", "birth"]
        )

        print("People born after 1957")
        for document in documents:
            print(document)
