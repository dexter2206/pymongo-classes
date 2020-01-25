from bson.json_util import loads
from pymongo import MongoClient


if __name__ == "__main__":
    # WARNING!!!!
    # THIS
    # DELETES
    # EVERYTHING
    with MongoClient() as client:
        client["products-db"]["products-info"].drop()

    with open("products.json") as products_file:
        documents = [loads(line) for line in products_file]

    with MongoClient() as client:
        products_info = client["products-db"]["products-info"]

        result = products_info.insert_many(documents)

        for _id in result.inserted_ids:
            product = products_info.find_one({"_id": _id})
            print(product["name"])
