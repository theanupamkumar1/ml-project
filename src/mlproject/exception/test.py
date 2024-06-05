import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import pandas as pd
from dotenv import load_dotenv
import pymongo

from src.mlproject.exception.logger import logging
from src.mlproject.exception.exception import CustomException

# Load environment variables
load_dotenv()
host = os.getenv("host")
password = os.getenv("password")
db_name = os.getenv("db_name")
username = os.getenv("username")
collection_name = os.getenv("collection_name")

def read_mongo_data():
    logging.info("Reading MongoDB data has started")
    try:
        # Try to use environment variables first
        # if all([host, password, db_name, username, collection_name]):
        #     uri = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority"
        #     logging.info(f"Attempting to connect to MongoDB using URI: {uri}")
        #     myclient = pymongo.MongoClient(uri)
        # else:
            # If environment variables are not set, use hardcoded values
        logging.warning("Environment variables not set. Using hardcoded values.")
        myclient = pymongo.MongoClient("mongodb+srv://memeslordak:dHWukrLt2ZcBCMR0@cluster0.9cm0c6m.mongodb.net/")
        
        try:
            # Test the connection
            myclient.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(f"Failed to ping MongoDB: {e}")
            return None
        
        # List all databases and collections
        print("Available databases:")
        for db in myclient.list_database_names():
            print(f"  - {db}")
            db_obj = myclient[db]
            print("    Collections:")
            for collection in db_obj.list_collection_names():
                print(f"      - {collection}")
        
        # Try to use the specified database and collection
        if db_name in myclient.list_database_names():
            mydb = myclient[db_name]
            if collection_name in mydb.list_collection_names():
                mycollection = mydb[collection_name]
                logging.info(f"Database '{db_name}' with collection '{collection_name}' is connected successfully")
                
                # Count documents and display a few
                doc_count = mycollection.count_documents({})
                print(f"\nFound {doc_count} documents in {db_name}.{collection_name}")
                
                if doc_count > 0:
                    print("First few documents:")
                    for doc in mycollection.find().limit(5):
                        print(doc)
                    
                    # Convert to DataFrame
                    data = list(mycollection.find())
                    df = pd.DataFrame(data)
                    print("\nDataFrame head:")
                    print(df.head())
                    print("\nDataFrame info:")
                    print(df.info())
                    
                    return df
                else:
                    print("No documents found in the collection.")
            else:
                print(f"Collection '{collection_name}' not found in database '{db_name}'.")
        else:
            print(f"Database '{db_name}' not found.")
            
        return None
    except Exception as e:
        error_msg = f"Error in read_mongo_data: {str(e)}"
        logging.error(error_msg)
        raise CustomException(error_msg)

if __name__ == "__main__":
    try:
        df = read_mongo_data()
        if df is not None:
            print("\nData retrieved successfully.")
        else:
            print("\nFailed to retrieve data.")
    except CustomException as ce:
        print(f"CustomException: {ce}")
    except Exception as e:
        print(f"Unexpected error: {e}")