# ── routes/parent.py ────────────────────────────────────────────
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.parent import Parent
from schemas.parent import ParentSignupRequest, ParentSignupResponse
from database import get_db
from utils.security import hash_password      # implement or stub it

router = APIRouter(prefix="/signup")

@router.post("/parent", response_model=ParentSignupResponse)
def signup_parent(data: ParentSignupRequest, db: Session = Depends(get_db)):
    # 1. basic validations
    if data.password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    if db.query(Parent).filter(Parent.phone == data.phone).first():
        raise HTTPException(status_code=400, detail="Phone already registered")

    if db.query(Parent).filter(Parent.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. create & persist
    new_parent = Parent(
        first_name=data.first_name,
        last_name=data.last_name,
        phone=data.phone,
        email=data.email,
        dob=data.dob,
        aadhaar_number=data.aadhaar_number,
        password=hash_password(data.password),
    )
    db.add(new_parent)
    db.commit()
    db.refresh(new_parent)

    # 3. return exactly what response_model expects
    return new_parent
