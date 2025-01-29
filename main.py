from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainigPipelineConfig


if __name__ == "__main__":
    try:
        
        trainigpipelineconfig = TrainigPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainigpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion initiated")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
        logging.info("Data ingestion completed")
    except Exception as e:
        raise NetworkSecurityException(e)
    