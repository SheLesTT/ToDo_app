
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base



Base = declarative_base()


class Task(Base):

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    content = Column(String, nullable=True)
    is_done = Column(Boolean, nullable=False, server_default='FALSE')

