#!/usr/bin/env python
import pandas as pd
import requests
import json
import psycopg2
import psycopg2.extras as extras
import os

def read_testing_data():
    CUR_DIR = os.path.abspath(os.path.dirname(__file__))
    data = pd.read_csv(str(CUR_DIR)+'/data/semiconductor_testing_data.csv')
    return data

def upload_csv_to_postgresql(db_params, table_name):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        
        df = read_testing_data()

        cursor.execute(f"""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = '{table_name}'
            );
        """)
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            columns = ', '.join([f'"{col}" VARCHAR' for col in df.columns])
            cursor.execute(f"""
                CREATE TABLE {table_name} ({columns});
            """)
            print(f"Table '{table_name}' created.")
        
        for index, row in df.iterrows():
            insert_query = f"""
                INSERT INTO {table_name} 
                VALUES ({', '.join(['%s'] * len(df.columns))});
            """
            cursor.execute(insert_query, tuple(row))
        
        conn.commit()
        print(f"Data uploaded to table '{table_name}'.")
    
    except Exception as e:
        print(f"Error: {e}")


def main():
    
    db_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'password',
        'host': 'host.docker.internal',
        'port': '5432'
    }
    
    table_name = 'semiconductor_testing_data'

    upload_csv_to_postgresql(db_params, table_name)

    print("Finished.")

if __name__ == "__main__":
    main()