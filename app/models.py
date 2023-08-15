
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from passlib import hash



Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)
    name = Column(String)

    def verify_password(self, password):
        return hash.bigcrypt.verify(password, self.hashed_password)
class Task(Base):

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    is_done = Column(Boolean, nullable=False, server_default='FALSE')

