from contextlib import asynccontextmanager
from sqlmodel import SQLModel, create_engine, Session
from . import models
from fastapi import FastAPI, Depends
from typing import Annotated
# should be hidden in ideal case
pgsql_url = f"postgresql://sannan:@localhost/inventory_db"

engine = create_engine(pgsql_url)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

