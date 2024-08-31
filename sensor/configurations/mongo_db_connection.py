import pymongo
from sensor.constants.database import DATABASE_NAME
import certifi

ca = certifi.where()

class MongoDBCLient:
    client = None 
    def __init__(self, database_name = DATABASE_NAME):
        try:
            if MongoDBCLient.client is None:
                mongo_db_url = "mongodb+srv://atikurrahman209:Atiqur786@phising.wnflnec.mongodb.net/?retryWrites=true&w=majority&appName=phising"
                MongoDBCLient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBCLient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e