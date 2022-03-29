
import sqlalchemy as db

engine = db.create_engine('postgresql://srv:0@localhost:5159/Dse')

connection = engine.connect()
query = '''SELECT  date,price,open,high,low,vol 
FROM 
asset JOIN price 
ON asset.id = price.asset_id 
WHERE 
date BETWEEN '{}' and '{}'
AND
symbol ='{}'
'''.format('2017-11-06 00:00:00','2020-08-18 00:00:00','BEACONPHAR')

result = connection.execute(query)

for r in result:
    print(r.date, "|", r.price, "|", r.high, "|", r.low)

