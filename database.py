from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/kiddo_db"  # Update with your values

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ✅ This is what must exist
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
