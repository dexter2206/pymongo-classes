from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        # Find people whose first name is John or last name is Ritche
        documents = biographies.find({"$or": [{"name.first": "John"}, {"name.last": "Ritchie"}]})

        print("> People with first name John or last name Ritchie")
        for document in documents:
            print(document["name"]["first"], document["name"]["last"])

        # Find people whose first name is John or Kristen
        documents = biographies.find({"name.first": {"$in": ["John", "Kristen"]}})

        print("> People with first name John or Kristen")
        for document in documents:
            print(document["name"]["first"], document["name"]["last"])
