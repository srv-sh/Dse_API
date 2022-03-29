from typing import Optional
import sqlalchemy as db
from datetime import datetime
import json
from model import Asset , Price



engine = db.create_engine('postgresql://srv:0@localhost:5159/Dse')

connection = engine.connect()


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/symbol/{symbol}")

def read_item(symbol: str, s: Optional[str] = '2008-03-17 00:00:00', e: Optional[str] = '2021-07-04 00:00:00' ):
    print("_______________")
    # print(symbol,"__________")
    print(s ,"_________",e)
    s = datetime.fromisoformat(s)
    e = datetime.fromisoformat(e)
    query = '''SELECT symbol,date,price,open,high,low,vol 
    FROM 
    asset JOIN price 
    ON asset.id = price.asset_id 
    WHERE 
    date BETWEEN '{}' and '{}'
    AND
    symbol ='{}'
    '''.format(s,e,symbol)
    result = connection.execute(query)
    # results = result.scalars().all()
    results ={}
    for r in result:
        results[str(r.date)] = {"price":r.price,"open":r.open,"high":r.high,"low":r.low,"vol":r.vol}
    json_object = json.dumps(results) 
    json_object = json.loads(json_object) 
    # print(type(json_object),"---------------")
    #return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]
    # print([Price(date = r.date, price = r.price,open = r.open, high = r.high, low = r.low, vol = r.vol) for r in result])
    # print(json_object)
    # return [Price(date = r.date, price = r.price,open = r.open, high = r.high, low = r.low, vol = r.vol) for r in results]
    # print(result)
    return json_object

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
