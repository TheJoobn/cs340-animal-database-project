import os
from pymongo import MongoClient


# CRUD operations for animal collection in MongoDB
class AnimalShelter:

    def __init__(self, username, password):
        HOST = os.getenv("MONGO_HOST")
        PORT = int(os.getenv("MONGO_PORT", "27017"))
        DB = os.getenv("MONGO_DB")
        COL = os.getenv("MONGO_COLLECTION")

        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d' % (username, password, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]


    # Insert document into MongoDB collection if data is valid
    def create(self, data):
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Insert failed: {e}")
        else:
            print("Nothing to save, data is empty.")

        return False


    # Return list of documents matching query
    def read(self, query):
        try:
            return list(self.collection.find(query))
        except Exception as e:
            print(f"Read failed: {e}")
            return []


    # Update information matching a query
    def update(self, query, update_data):
        try:
            result = self.collection.update_many(
                query,
                {"$set": update_data}
            )
            return result.modified_count
        except Exception as e:
            print(f"Update failed: {e}")
            return 0


    # Delete documents matching a query
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete failed: {e}")
            return 0
