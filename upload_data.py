from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource indentifier
uri = "mongodb+srv://milanbeherazyx:VKF4Yq7WqLwGIpkG@cluster0.wui6u7y.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="Project"
COLLECTION_NAME="Concrete_Compressive_Prediction"

# read the data as a dataframe
df = pd.read_csv(r"/home/milanbeherazyx/Data Science/Concrete_Compressive_Prediction/notebooks/data/concrete_data.csv")


# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)