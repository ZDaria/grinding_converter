from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import configparser

config = configparser.ConfigParser()
config.read("../configs/db.ini")

engine = create_engine(config['DEFAULT']['db_string'])
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
