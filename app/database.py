import logging

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from starlette.requests import Request

log = logging.getLogger(__file__)


engine = create_engine(f"postgresql+psycopg2://guest:guest@localhost:5431/testdb")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db(request: Request):
    return request.state.db
