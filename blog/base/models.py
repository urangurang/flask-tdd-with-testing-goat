from sqlalchemy import Column, String, Integer
from blog.database import Base


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(40))

    def __init__(self, text):
        self.text = text


