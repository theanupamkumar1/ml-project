import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.mlproject.exception.exception import CustomException
from src.mlproject.exception.logger import logging
# from .logger import logging
# from .exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymongo

import pickle
import numpy as np


load_dotenv()
host=os.getenv("host")
password=os.getenv("password")
db_name=os.getenv("db_name")
username=os.getenv("username")
collection_name=os.getenv("collection_name")

def read_mongo_Data():
    logging.info("reading monogo db has started")
    try:

        # uri = f"mongodb+srv://memeslordak:{password}@cluster0.9cm0c6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # myclient = pymongo.MongoClient(f"mongodb://{username}:{password}@{host}")
       
        # myclient = pymongo.MongoClient("localhost", 27017)
        
        myclient = pymongo.MongoClient(f"mongodb+srv://memeslordak:dHWukrLt2ZcBCMR0@cluster0.9cm0c6m.mongodb.net/")

        try:
            myclient.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB database nigga!")
        except Exception as e:
            print(e)
        
        db_list = myclient.list_database_names()
        if db_name in db_list:
            mydb = myclient[db_name]

            mycollection = mydb[collection_name]
            logging.info(f"database{db_name} with collection named{collection_name} is  connected succesfully")
            data = mycollection.find()
            
            # Convert to DataFrame
            df = pd.DataFrame(list(data))
            print(df.head())
            
            return df


        else:
            raise Exception("The database does not exist.")
    except Exception as e:
        raise CustomException()


def save_object(file_path,obj):
    try:
        dir_path =os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open  (file_path, "wb") as file_obj:
            pickle.dump(obj,file_obj)
        



    except Exception as e:
        raise CustomException(e,sys)