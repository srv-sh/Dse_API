from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Asset , Price
from datetime import date, datetime
import pandas as pd
import os
import uuid
def generate_uuid():
    return str(uuid.uuid4())
session_maker = sessionmaker(bind=create_engine("postgresql://srv:0@localhost:5159/Dse"))
BASE_DIR = "G:/clean_dataset/"
files = os.listdir(BASE_DIR)
with session_maker() as session:
    for file in files:
        symbol_name = file.split('.')[0]
        df = pd.read_csv(BASE_DIR + file)
        df.drop('Unnamed: 0',axis=1,inplace=True)

        for idx , row in df.iterrows():
            asset = Asset(id = generate_uuid() , symbol = symbol_name )
            price = Price(date = row[0] ,price = row[1] ,open = row[2], high = row[3] , low = row[4],vol = row[5], asset_id = asset.id)
            asset.prices = [price]
            session.add(asset)
            session.add(price)
            print(asset ,'--------', price.asset_id)    
        session.commit()
        # print(asset ,--------, price.asset_id)
# print(generate_uuid())




