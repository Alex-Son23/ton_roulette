from sqlalchemy import Column, BigInteger, DateTime, String, Integer, Boolean, Float

from .__base__ import MyBaseModel

class Draw(MyBaseModel):
    __tablename__ = "draw"

    id = Column(Integer, autoincrement=True, primary_key=True)
    winning_name = Column(String)
    win_percentage = Column(Float)
    dis_percentage = Column(Float)

    # Новые поля для диапазонов и ссылки
    min_amount = Column(Float, nullable=False, default=0.0)
    max_amount = Column(Float, nullable=False, default=999999.0)
    gifts_link = Column(String, nullable=True)

    def __repr__(self):
        return MyBaseModel.__repr__(self)
