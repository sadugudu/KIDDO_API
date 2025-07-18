from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base  # ✅ THIS IS REQUIRED

Base = declarative_base()  # ✅ DEFINE Base here

class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    dob = Column(Date, nullable=False)
    aadhaar_number = Column(String(12), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
