from sensor.configurations.mongo_db_connection import MongoDBCLient
from sensor.exception import CustomException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
import sys
from sensor.pipleline.training_pipeline import TrainPipeline
from sensor.components.data_ingestion import DataIngestion
def test():
    try:
        1/0
    except Exception as e:
            raise CustomException(e, sys)


if __name__=='__main__':
    # mongodb_client = MongoDBCLient()
    # print(mongodb_client.database.list_collection_names())
    # try:
    #      test()
    # except Exception as e:
    #      logging.info("Exception occured ")
    #      print(e)
    # trainiing_pipleine_config = TrainingPipelineConfig()
    # data_ingestion_config = DataIngestionConfig()

    # print(data_ingestion_config.__dict__)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipleine()
