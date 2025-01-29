from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime
import os

from scripts.upload_to_mongodb_ETL import upload_csv_to_mongodb 

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
CSV_FILE_PATH = os.path.join(CUR_DIR, Variable.get("csv_file_path", 'scripts/data/semiconductor_testing_data.csv')) 
MONGO_COLLECTION = Variable.get("mongo_collection", 'semiconductor_testing_data')

with DAG(
    dag_id='extract_to_mongodb_DAG',
    schedule_interval='@once',
    start_date=datetime(2024, 10, 25),
    catchup=False,
) as dag:
    
    upload_task = PythonOperator(
        task_id='upload_csv',
        python_callable=upload_csv_to_mongodb,
        op_kwargs={
            'csv_file_path': CSV_FILE_PATH,
            'mongo_host': 'mongodb',
            'mongo_port': 27017,
            'mongo_db': 'semiconductor_testing',
            'mongo_collection': MONGO_COLLECTION
        },
    )

upload_task
