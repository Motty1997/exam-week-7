from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings.config import DB_URL


engin = create_engine(DB_URL)
session_maker = sessionmaker(bind=engin)

