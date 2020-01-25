from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        # Find number of records with name.first starting with "J"
        count = biographies.count_documents({"name.first": {"$regex": "^J"}})

        print(f"There are {count} people with first name starting with J")
