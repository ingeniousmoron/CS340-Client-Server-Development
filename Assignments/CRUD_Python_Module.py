# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS, DB, COL): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        HOST = 'localhost' 
        PORT = 27017
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            result = self.collection.insert_one(data)  # data should be dictionary
            if result.inserted_id:
                return True
            else:
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None: 
            result = list(self.collection.find(data))  # data should be dictionary
        else:
            result = self.collection.find({},{"_id": False})
        return result
            
    # Create method to implement the U in CRUD.
    def update(self, data, update_data):
        if data is not None:
            result = self.collection.update_many(data, update_data)
            if (result.modified_count > 1 or result.modified_count == 0):
                ("modified", result.modified_count, "results")
            elif (result.modified_count == 1):
                ("modified 1 result")
        return result
    
    # Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            result = self.collection.delete_many(data) # data should be dictionary
            if (result.deleted_count > 1 or result.deleted_count == 0):
                print ("deleted", result.deleted_count, "results")
            elif (result.deleted_count == 1):
                print ("deleted 1 result")
            return result
            
