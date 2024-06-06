from src.mlproject.exception.logger import logging
from src.mlproject.exception.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.model_trainer import ModelTrainer

import os 
import sys

if __name__=="__main__":
    

    try:
        
        data_ingetion= DataIngestion()
        train_data_path, test_data_path =data_ingetion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr, test_arr, _=data_transformation.initiate_data_transormation(train_data_path, test_data_path )

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer( train_arr,test_arr))
        


    except Exception as e:
        raise CustomException(e,sys)