from bson import json_util
from pprint import pprint
from pymongo import MongoClient


if __name__ == "__main__":
    # Open file for reading
    with open("biographies.json") as biographies_file:
        # Load biographies. note that we use json_util module.
        # It offers several advantages including decoding dates
        documents = json_util.loads(biographies_file.read())

    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        # Insert multiple documents
        result = biographies.insert_many(documents)

        # Iterate over inserted ids, retrieve each document by id and see if
        # the data is ok.
        for _id in result.inserted_ids:
            document = biographies.find_one({"_id": _id})
            pprint(document)
