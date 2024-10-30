#!/usr/bin/env python
import pandas as pd
import requests
import json
import psycopg2
import psycopg2.extras as extras
import os

def read_testing_data():
    CUR_DIR = os.path.abspath(os.path.dirname(__file__))
    d1_data = pd.read_csv(str(CUR_DIR)+'/data/D1.csv')
    d2_data = pd.read_csv(str(CUR_DIR)+'/data/D2.csv')
    return d1_data, d2_data

def create_table(conn):
    cur = conn.cursor() 
    try:
        cur.execute("""DROP TABLE IF EXISTS d1_semiconductor_testing_data;
        CREATE TABLE IF NOT EXISTS d1_semiconductor_testing_data (
            MaterialID INT,
            StepID INT,
            duration_ms FLOAT,
            feature_1 FLOAT,
            feature_2 FLOAT,
            feature_3 FLOAT,
            feature_4 FLOAT,
            feature_5 FLOAT,
            feature_6 FLOAT,
            feature_7 FLOAT,
            feature_8 FLOAT,
            feature_9 FLOAT,
            feature_10 FLOAT,
            feature_11 FLOAT,
            feature_12 FLOAT,
            feature_13 FLOAT,
            feature_14 FLOAT,
            feature_15 FLOAT,
            is_test INT,
            target INT
        );

        DROP TABLE IF EXISTS d2_semiconductor_testing_data;
        CREATE TABLE IF NOT EXISTS d2_semiconductor_testing_data (
            MaterialID INT,
            StepID INT,
            duration_ms FLOAT,
            feature_1 FLOAT,
            feature_2 FLOAT,
            feature_3 FLOAT,
            feature_4 FLOAT,
            feature_5 FLOAT,
            feature_6 FLOAT,
            feature_7 FLOAT,
            feature_8 FLOAT,
            feature_9 FLOAT,
            feature_10 FLOAT,
            feature_11 FLOAT,
            feature_12 FLOAT,
            feature_13 FLOAT,
            feature_14 FLOAT,
            feature_15 FLOAT,
            feature_16 FLOAT,
            feature_17 FLOAT,
            feature_18 FLOAT,
            feature_19 FLOAT,
            feature_20 FLOAT,
            is_test INT,
            target INT
        );

        """)
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error) 
        conn.rollback()
    else:
        conn.commit()

def insert_values(conn, df, table):
    print(type(df))
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns)) 
    query = """INSERT INTO %s(%s) VALUES %%s;""" % (table, cols) 
    cursor = conn.cursor() 
    try: 
        extras.execute_values(cursor, query, tuples) 
        conn.commit() 
    except (Exception, psycopg2.DatabaseError) as error: 
        print("Error: %s" % error) 
        conn.rollback() 
        cursor.close() 
        return 1
    cursor.close()

def main():
    
    conn = psycopg2.connect(
        host="host.docker.internal", 
        database="postgres",
        user="postgres",
        password="password")
     
    print("Transforming...")
    create_table(conn)
    d1_data, d2_data = read_testing_data()
    print(d1_data, d2_data)
    print("Loading...")
    insert_values(conn, d1_data, 'd1_semiconductor_testing_data')
    insert_values(conn, d2_data, 'd2_semiconductor_testing_data')
    print("Finished.")

if __name__ == "__main__":
    main()