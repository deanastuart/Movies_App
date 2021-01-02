from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import Column, Integer, String, Numeric

Base = declarative_base()

class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer)
    original_title = Column(String)
    actor_name = Column(String)
    billing_order = Column(Integer)
    actor_and_movie = Column(String, primary_key=True)

    def __init__(self, id, original_title, actor_name, billing_order, actor_and_movie):
        self.id = id
        self.original_title = original_title
        self.actor_name = actor_name
        self.billing_order = billing_order
        self.actor_and_movie = actor_and_movie