from fastapi import FastAPI, APIRouter, HTTPException
import pandas as pd
import pymongo
import os
from dotenv import load_dotenv

AutomateRoute = APIRouter()
load_dotenv()


data= pd.read_csv('fullData.csv')


client = pymongo.MongoClient(os.gotenv("MONGO_URI")) 
db = client.get_database()

COLLECTION_NAME1 = "Charts"
collection = db[COLLECTION_NAME1]

COLLECTION_NAME2 = "Users"
collection2 = db[COLLECTION_NAME2]

COLLECTION_NAME3 = "Forecast"
collection3 = db[COLLECTION_NAME3]

COLLECTION_NAME4 = "Top20s"
collection4 = db[COLLECTION_NAME4]

COLLECTION_NAME5 = "Negative"
collection5 = db[COLLECTION_NAME5]
