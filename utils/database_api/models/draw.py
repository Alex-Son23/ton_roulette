from sqlalchemy import Column, BigInteger, DateTime, String, Integer, Boolean, Float

from .__base__ import MyBaseModel

class Draw(MyBaseModel):
    __tablename__ = "draw"

    id = Column(Integer, autoincrement=True, primary_key=True)
    winning_name = Column(String)
    win_percentage = Column(Float)
    dis_percentage = Column(Float)

    def __repr__(self):
        return MyBaseModel.__repr__(self)
