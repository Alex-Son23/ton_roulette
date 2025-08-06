from sqlalchemy import Column, BigInteger, DateTime, String, Integer, Boolean, Float

from .__base__ import MyBaseModel


class Log(MyBaseModel):
    __tablename__ = "log"

    id = Column(Integer, autoincrement=True, primary_key=True)
    address = Column(String)
    winning_name = Column(String)
    id_trans = Column(String)
    amount = Column(String)
    date_register = Column(DateTime)

    def __repr__(self):
        return MyBaseModel.__repr__(self)
