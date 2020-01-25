from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        # Find all people that received Turing Award
        documents = biographies.find({"awards": {"$elemMatch": {"award": "Turing Award"}}}, ["name.last", "awards.award"])

        for document in documents:
            print(document["name"]["last"], document["awards"])
