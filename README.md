## **Project Title**
Orchestrating Semiconductor Data Pipelines Using Airflow


# Airflow DAGs for Semiconductor Testing and ML Execution

This project contains three Apache Airflow DAGs designed for executing ETL tasks and running machine learning algorithms. The DAGs are:

1. **semiconductor_testing_DAG** - Runs an ETL process for semiconductor testing data.
2. **extract_to_mongodb_DAG** - Extracts semiconductor testing data from a CSV file and loads it into MongoDB.
3. **ml_algorithms_execution** - Executes machine learning algorithms (XGBoost and RandomForest).

## Prerequisites
- Docker and Docker Compose installed
- Airflow set up with a Dockerized environment
- MongoDB running as a service (included in `docker-compose.yml`)

## How to Run

### 1. Start Airflow with Docker
Run the following command in the project directory:
```bash
docker-compose up -d
```
This will start all necessary Airflow services.

### 2. Access the Airflow Web UI
Once Airflow is running, open the web UI at:
```
http://localhost:8080
```
Use the default credentials:
- Username: `airflow`
- Password: `airflow`

### 3. Trigger the DAGs
Navigate to the **DAGs** tab in Airflow UI and enable the following DAGs:
- `semiconductor_testing_DAG`
- `extract_to_mongodb_DAG`
- `ml_algorithms_execution`

Alternatively, trigger them via the command line:
```bash
airflow dags trigger semiconductor_testing_DAG
airflow dags trigger extract_to_mongodb_DAG
airflow dags trigger ml_algorithms_execution
```

### 4. Monitor DAG Execution
Check task progress in the **Graph View** or **Task Instance** section of each DAG in the Airflow UI.

## DAG Details

### 1. **semiconductor_testing_DAG**
- Runs `Semiconductor_Testing_ETL.py` via a Bash task.
- Processes semiconductor testing data for further analysis.

### 2. **extract_to_mongodb_DAG**
- Extracts semiconductor testing data from a CSV file.
- Loads the data into a MongoDB collection.
- Uses the `upload_to_mongodb_ETL.py` script.

### 3. **ml_algorithms_execution**
- Executes machine learning models sequentially:
  - XGBoost
  - RandomForest
- Uses Bash tasks to run the respective Python scripts.

## Stopping the Services
To stop all Airflow services, run:
```bash
docker-compose down
```