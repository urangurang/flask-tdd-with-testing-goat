from sqlalchemy import Column, String, Integer, ForeignKey
from blog.database import Base


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(40))
    list = Column(Integer, ForeignKey('list.id'))

    def __init__(self, text, list):
        self.text = text
        self.list = list


class List(Base):
    __tablename__ = 'list'

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self):
        pass