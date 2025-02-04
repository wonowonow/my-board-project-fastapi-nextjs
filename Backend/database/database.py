import os
from Backend.Model.Post import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()