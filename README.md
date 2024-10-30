## **Project Title**
Orchestrating Semiconductor Data Pipelines Using Airflow

## **Introduction**
This project automates data extraction, transformation, and storage using Apache Airflow. It includes two distinct Directed Acyclic Graphs (DAGs):

## **Features**
Data Extraction DAG: Schedules and triggers ETL processes for semiconductor testing data.
MongoDB Upload DAG: Handles the upload of CSV files to MongoDB for further analysis.
Project Structure
semiconductor_testing_DAG: Executes a Bash script for the ETL process every 30 minutes.
extract_to_mongodb_DAG: Runs a one-time Python task to load CSV data into MongoDB.

## **Getting Started**
Install Dependencies: Requires Airflow, MongoDB, and necessary Python packages.
Configure Variables: Set csv_file_path and mongo_collection in Airflow Variables.
Usage
Deploy the DAGs to Airflow and monitor their status via the Airflow UI.
DAGs automatically retrieve data and load it into MongoDB for further processing and analysis.