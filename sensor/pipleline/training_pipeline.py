from sensor.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from sensor.exception import CustomException
import sys
from sensor.logger import logging
from sensor.entity.artificat_entity import DataIngestionArtifact
from sensor.components.data_ingestion import DataIngestion

class TrainPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingstion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion COmpletetd and artifacts: {data_ingstion_artifact}")
            return data_ingstion_artifact
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
    
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
    
    def strt_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
    
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
    
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
    
    
    
    def run_pipleine(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact =self.start_data_ingestion()
        except Exception as e:
            raise CustomException(e, sys)
    
