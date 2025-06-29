from pymongo import MongoClient
from bson.objectid import ObjectId

#CRUD operaters for animal collection in mongoDB
class AnimalShelter:

    #initialize connection to MongoDB - change variables
    def __init__(self, username, password):
        USER = username
        PASS = password

        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31846
        DB = 'AAC'
        COL = 'animals'

        #Connection to Database
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
#---------------------------------------------------------------------------------------------
    #Insert document into MongoDB collection if data is valid
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
#---------------------------------------------------------------------------------------------
    #Return list of documents matching query
    def read(self, query):
        try:
            return list(self.collection.find(query))
        except Exception as e:
            print(f"Read failed: {e}")
            return []
#---------------------------------------------------------------------------------------------        
    #Update infomration for a query
    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            print(f"Update failed: {e}")
            return 0
#---------------------------------------------------------------------------------------------            
    #Delete a query
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete failed: {e}")
            return 0
        
        
        
        
        