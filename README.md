# MLProject

MLProject is a machine learning project that includes data ingestion, data transformation, model training, and model monitoring components. It is designed to be scalable and easy to use.

## key data Components

The project is divided into several components, each responsible for a specific task:

- `data_ingestion.py`: Responsible for ingesting data.
- `data_transformation.py`: Transforms the ingested data.
- `model_trainer.py`: Trains a machine learning model on the transformed data.
- `model_monitoring.py`: Monitors the performance of the trained model.

## Project Structure

- `.dvc/`: Contains DVC files for data versioning.
- `.ebextensions/`: Contains configuration files for AWS Elastic Beanstalk. The `python.config` file sets the WSGIPath to `application:application`.
- `artifacts/`: Contains serialized machine learning models and data files.
- `mlruns/`: Contains metadata about MLflow runs.
- `src/`: Contains the source code of the application.

## Key Files

- `application.py`: The main entry point of the application.
- `Dockerfile`: Used to create a Docker image of the application.
- `requirements.txt`: Lists the Python packages that the project depends on.

## Setup

To set up the project, you need to install the dependencies listed in the `requirements.txt` file. You can do this by running:

```bash
pip install -r requirements.txt


```

## Usage

The main entry point of the application is application.py. You can run it with:

python application.py

# Project Components

## Data Version Control (DVC)

Your project uses DVC for data versioning. The `.dvc` directory and `.dvcignore` file are used for this purpose.

## Elastic Beanstalk Configuration

The `.ebextensions` directory contains configuration files for AWS Elastic Beanstalk. The `python.config` file sets the WSGIPath to `application:application`.

## Python Application

The `application.py` file is the main entry point of your application. It imports various components from the `src` directory and defines several routes for a Flask application.

## Machine Learning Artifacts

The `artifacts` directory contains serialized machine learning models (`model.pkl` and `preprocessor.pkl`) and data files (`raw.csv`, `test.csv`, `train.csv`).

## MLflow Runs

The `mlruns` directory contains metadata about MLflow runs. Each run has a unique ID and contains information such as the user who initiated the run, the start and end times, and the location of any artifacts produced during the run.

## Dockerfile

The Dockerfile is used to create a Docker image of your application.

## Requirements

The `requirements.txt` file lists the Python packages that your project depends on.

## Source Code

The `src` directory contains the source code of your application. It includes various components such as data ingestion, data transformation, and model training.
