from datetime import datetime

from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        documents = biographies.find(
            {
                "$or": [
                    {"contribs": "Fortran"},
                    {"awards": {"$elemMatch": {"award": "Turing Award"}}},
                ]
            }
        )

        for document in documents:
            print(document)
