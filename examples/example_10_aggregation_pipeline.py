from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient(host="localhost", port=27017) as client:
        db = client["biographies-database"]

        biographies = db["biographies"]

        # Find total numbers of awards for each distinct award
        documents = biographies.aggregate(
            [{"$unwind": "$awards"}, {"$group": {"_id": "$awards.award", "total": {"$sum": 1}}}]
        )

        print("> Awards and total number they were awarded")
        for document in documents:
            print(f"{document['_id']} awarded {document['total']} times.")
