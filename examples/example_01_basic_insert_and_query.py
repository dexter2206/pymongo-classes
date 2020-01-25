from datetime import datetime
from pprint import pprint
from pymongo import MongoClient


if __name__ == "__main__":
    # Construct client - it can be used as context manager
    with MongoClient(host="localhost", port=27017) as client:
        # Get database named "biographies-database"
        db = client["biographies-database"]

        # Get collection named "biographies"
        biographies = db["biographies"]

        # Create document using standard Python data types
        document = {
            "name": {
                "first": "Martin",
                "last": "Odersky"
            },
            "contribs": [
                "Scala"
            ],
            "birth": datetime(1958, 9, 5)
        }

        # Insert document
        result = biographies.insert_one(document)

        # See that some id was assigned to the object
        print("ID assigned to document:", result.inserted_id)

        # Retrieve the same object
        retrieved_document = biographies.find_one({"_id": result.inserted_id})

        pprint(retrieved_document)