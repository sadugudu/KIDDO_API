from fastapi import FastAPI
from database import Base, engine
from routes import parent as parent_route
from models import parent
from database import engine

parent.Base.metadata.create_all(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(parent_route.router)
