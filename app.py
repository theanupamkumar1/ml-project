from src.mlproject.exception.logger import logging
from src.mlproject.exception.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig

import os 
import sys

if __name__=="__main__":
    
    


    try:
        data_ingetion= DataIngestion()
        data_ingetion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e,sys)