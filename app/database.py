from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.orm import sessionmaker, declarative_base
from app.models import Task , Base

DATABASE_URL = "postgresql://postgres:F_7d3fd73@localhost:5432/note_app"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

s =Session()

# a = Task(id =  2,name= "test",content  = "test",is_done=False)
# s.add(a)
# s.commit()
# task = s.query(Task).filter(Task.id == 1).first()
# print(task.content)
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
