import dagshub
dagshub.init(repo_owner='theanupamkumar1', repo_name='ml-project', mlflow=True)

import mlflow
with mlflow.start_run():
mlflow.log_param('parameter name', 'value')
mlflow.log_metric('metric name', 1)

MLFLOW_TRACKING_URI=https://dagshub.com/theanupamkumar1/ml-project.mlflow
MLFLOW_TRACKING_USERNAME=theanupamkumar1
MLFLOW_TRACKING_PASSWORD= 9b08b538ddfac3b1a5e93e7387fa624d4025691b
python script.py
