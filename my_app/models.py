from my_app import db
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql.json import JSONB


class Form(db.Model):
  __tablename__ = 'forms'
  id = Column(Integer, primary_key=True, autoincrement=True)
  names = Column(JSONB)
  
  def __init__(self, names):
    self.names = names
 