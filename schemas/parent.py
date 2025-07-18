from pydantic import BaseModel, EmailStr
from datetime import date

class ParentSignupRequest(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    dob: date
    aadhaar_number: str
    password: str
    confirm_password: str

class ParentSignupResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    dob: date
    aadhaar_number: str

    class Config:
        from_attributes = True  # or orm_mode = True for older Pydantic versions
