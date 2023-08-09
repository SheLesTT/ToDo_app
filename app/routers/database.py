from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:F_7d3fd73@localhost:5432/note_app"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()
result = session.execute('SELECT * FROM users')
for row in result:
    print(row)