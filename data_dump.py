import pymongo
import pandas as pd
import json
from sensor.config import mongo_client

DATE_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATE_FILE_PATH) 
    print(f"Rows and Columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongodb
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #Insert converted json record to mongodb
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    #client = MongoClient('mongodb+srv://Akshaygp:agastya123@cluster0.4k1lcs8.mongodb.net/?retryWrites=true&w=majority')

    #database_name = client['aps']

    #collection = database_name['sensor']

    #collection.insert_many(records)
