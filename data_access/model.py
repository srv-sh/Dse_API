from email.policy import default
from lib2to3.pytree import Base
from sqlalchemy import Column, String , DateTime, Integer, Float , ForeignKey,PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base , relationship
import uuid

def generate_uuid():
    return str(uuid.uuid4())


Base = declarative_base()

class Asset(Base):
    __tablename__ = "asset"
    id = Column(String, primary_key=True,nullable=False,default = generate_uuid)
    # date = Column(DateTime , nullable = False)
    symbol = Column(String , nullable = False)
    prices = relationship("Price")

    def dict(self):
        return {
            "id" : self.id,
            "symbol" : self.symbol,
            "prices" : self.prices
        }


class Price(Base):
    __tablename__ = "price"
    id = Column(String, primary_key=True, default=generate_uuid)
    date = Column(DateTime , nullable = False)
    price = Column(Float)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    vol = Column(Float)
    asset_id = Column(String, ForeignKey("asset.id"))

    def dict(self):
        return{
            "id" : self.id,
            "date" : self.date,
            "price" : self.price,
            "open" : self.open ,
            "high" : self.high,
            "low" : self.low,
            "vol" : self.vol 
        }



