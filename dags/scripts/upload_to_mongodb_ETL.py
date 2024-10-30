
from pymongo import MongoClient
import pandas as pd

def upload_csv_to_mongodb(csv_file_path, mongo_host='mongodb', mongo_port=27017, mongo_db='your_db_name', mongo_collection='your_collection_name'):
    df = pd.read_csv(csv_file_path)
    
    client = MongoClient(mongo_host, mongo_port)
    db = client[mongo_db]
    collection = db[mongo_collection]

    collection.insert_many(df.to_dict(orient='records'))
    client.close()
