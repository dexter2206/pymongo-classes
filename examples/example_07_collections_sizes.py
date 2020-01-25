from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        # Find all people who got exactly 3 awards
        documents = biographies.find({"awards": {"$size": 3}}, ["name.last", "awards.award"])

        print("> Documents with three awards:")
        for document in documents:
            awards = [record["award"] for record in document["awards"]]
            print(document["name"]["last"], awards)

        # Find all people who got less them 3 awards
        documents = biographies.find({"awards.2": {"$exists": False}})
        print("> Documents with less than three awards:")
        for document in documents:
            if "awards" in document:
                awards = [record["award"] for record in document["awards"]]
            else:
                awards = []
            print(document["name"]["last"], awards)

        # Find all people who got less them 3 awards
        documents = biographies.find({"awards.3": {"$exists": True}})
        print("> Documents with more than three awards:")
        for document in documents:
            awards = [record["award"] for record in document["awards"]]
            print(document["name"]["last"], awards)
