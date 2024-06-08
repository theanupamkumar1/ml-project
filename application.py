from src.mlproject.exception.logger import logging
from src.mlproject.exception.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.model_trainer import ModelTrainer
from flask import Flask,request,render_template,jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.mlproject.pipelines.prediction_pipeline import CustomData,PredictPipeline

import os 
import sys 
    
application=Flask(__name__)

app=application

## Route for a home page

try:
    
    data_ingetion= DataIngestion()
    train_data_path, test_data_path =data_ingetion.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _=data_transformation.initiate_data_transormation(train_data_path, test_data_path )

    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_trainer( train_arr,test_arr))

    
    


except Exception as e:
    raise CustomException(e,sys)




@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        logging.info("predicted result using web-interface")
        return render_template('home.html',results=results[0])
    
@app.route('/api',methods=['GET','POST'])

def predict_using_api():
    
    data = request.get_json()
    pred_df = pd.DataFrame([data])
    print(pred_df)
    print("Before Prediction")

    predict_pipeline=PredictPipeline()
    print("Mid Prediction")
    results=predict_pipeline.predict(pred_df)
    print("after Prediction")
    logging.info("predicted result using api")
    return jsonify(results=results[0])









if __name__=="__main__":
    app.run(host="0.0.0.0")      




