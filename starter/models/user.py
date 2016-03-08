from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )
from ..models.meta import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    full_name = Column(Text)

Index('my_index', User.name, unique=True, mysql_length=255)
