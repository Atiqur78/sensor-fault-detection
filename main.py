from sensor.configurations.mongo_db_connection import MongoDBCLient
from sensor.exception import CustomException
from sensor.logger import logging
import sys
def test():
    try:
        1/0
    except Exception as e:
            raise CustomException(e, sys)


if __name__=='__main__':
    # mongodb_client = MongoDBCLient()
    # print(mongodb_client.database.list_collection_names())
    try:
         test()
    except Exception as e:
         logging.info("Exception occured ")
         print(e)