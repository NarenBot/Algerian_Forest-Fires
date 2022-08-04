import pymongo

class MongodbConnection:
    # Initialization of MongoDB Atlas
    def __init__(self, username, password) -> None:
        try:
            self.username = username
            self.password = password
            self.url = f"mongodb+srv://{self.username}:{self.password}@cluster10.odazv.mongodb.net/?retryWrites=true&w=majority"
        except Exception as e:
            raise e

    def getMongoClient(self):
        try:
            client = pymongo.MongoClient(self.url)
            return client
        except Exception as e:
            raise e

    def getDatabase(self, dbName):
        try:
            client = self.getMongoClient()
            database = client[dbName]
            return database
        except Exception as e:
            raise e

    def getCollection(self, dbName, collectionName):
        try:
            db = self.getDatabase(dbName)
            collection = db[collectionName]
            return collection
        except Exception as e:
            raise e

    def getData(self, dbName, collectionName):
        try:
            database = self.getDatabase(dbName)
            collection = database[collectionName]
            cursor = collection.find()
            list_cursor = list(cursor)
            return list_cursor
        except Exception as e:
            raise e

